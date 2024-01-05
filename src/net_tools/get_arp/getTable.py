import os
import re
import json
import datetime 
import toml


def execute_bash(name, ip, net_tools_folder, username):
    if os.path.exists(f"{net_tools_folder}/GetARP/arp_tables/{name}/") is True:
        print("répertoire existant")
    else:
        os.system(f"mkdir -p {net_tools_folder}/GetARP/arp_tables/{name}")
    cmd = (
        f'ssh -o "StrictHostKeyChecking no" {username}@{ip} -p 8022 -t '
        f'"arp -a">{net_tools_folder}/GetARP/arp_tables/{name}/"{name}"_arp_table.txt'
    )
    print(os.system(cmd))
    return f"{name}_arp_table.txt"


def read_table(table, name, net_tools_folder):
    lines = []
    infos = []
    arp_table = open(f"{net_tools_folder}/GetARP/arp_tables/{name}/{table}")
    lines.append(arp_table)
    print(lines)
    for line in lines:
        temp = []
        for info in line:
            temp.append(re.sub("\n", "", info))
        infos.append(temp)
    return infos


def parse_table(table):
    print(table)
    table = table[0]
    dico = {}
    for info in table:
        temp = {}
        mac = info.split(" at ")[1].split(" on ")[0]
        ip = info.split(" at ")[0].split("(")[1].split(")")[0]
        name = info.split(" at ")[0].split(" (")[0]
        if name == "?":
            temp[ip] = "Name-Unknown"
        else:
            temp[ip] = name
        dico[mac] = temp
    return dico


def create_json(name, dico, net_tools_folder):
    liste = [dico]
    today = datetime.datetime.now()
    if os.path.exists(f"{net_tools_folder}/GetARP/arp_tables/{name}/json/") != True:
        os.system(f"mkdir {net_tools_folder}/GetARP/arp_tables/{name}/json/")
    f = open(f"{net_tools_folder}/GetARP/arp_tables/{name}/json/{name}_{today}.json", "w")
    f.write(json.dumps(liste))


def create_markdown(name, dico, net_tools_folder):
    today = datetime.datetime.now()
    if os.path.exists(f"{net_tools_folder}/GetARP/arp_tables/{name}/markdown") != True:
        os.system(f"mkdir {net_tools_folder}/GetARP/arp_tables/{name}/markdown")
    f = open(f"{net_tools_folder}/GetARP/arp_tables/{name}/markdown/{name}_{today}.md", "w")
    f.write("| MAC @ | IP @ | Name |" + "\r")
    f.write("| :---: | :---: | :---: |" + "\r")
    for cle in dico.keys():
        mac = cle
        ip = ""
        name = ""
        sub_dico = dico[cle]
        for sub_key in sub_dico:
            ip = sub_key
            name = sub_dico[sub_key]
        f.write(f"| {mac} | {ip} | {name} |" + "\r")
    f.close()


def main(name, ip, conf):
    net_tools_folder = toml.load(conf)["repositories"]["net_tools_folder"]
    username = toml.load(conf)["user"]["username"]
    table = execute_bash(name, ip, net_tools_folder, username)
    txt = read_table(table, name, net_tools_folder)
    parsed = parse_table(txt)
    create_json(name, parsed, net_tools_folder)
    create_markdown(name, parsed, net_tools_folder)