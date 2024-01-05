import os
import datetime
import toml


def execute_bash(name, ip, net_tools_folder, username):
    today = datetime.datetime.now()
    if os.path.exists(f"{net_tools_folder}/GetConfig/conf_xml/{name}") is True:
        print("répertoire existant")
    else:
        os.system(f"mkdir -p {net_tools_folder}/GetConfig/conf_xml/{name}")
    cmd = (
        f'scp -P 8022 {username}@{ip}:/conf/config.xml {net_tools_folder}/GetConfig/conf_xml/{name}/"{name}_{today}".xml'
    )
    print(cmd)
    os.system(cmd)
    os.system(f"ls {net_tools_folder}/GetARP/arp_tables > {net_tools_folder}/liste.txt")
    return f"{name}_arp_table.txt"



def main(name, ip, conf):
    net_tools_folder = toml.load(conf)["repositories"]["net_tools_folder"]
    username = toml.load(conf)["user"]["username"]
    execute_bash(name, ip, net_tools_folder, username)