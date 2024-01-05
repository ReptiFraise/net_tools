import json
<<<<<<<< HEAD:src/net_tools/compare_arp/compare.py
import toml
import os
========

REPO = "./src/GetARP/Tables_json/"
>>>>>>>> master:src/CompareARP/compare.py

def str_to_dico(table):
    t = open(table,"r")
    jsonStr = t.readline()
    dico = json.loads(jsonStr)[0]
    t.close
    return dico
    

def compare_dicos(dico1, dico2, conf):
    cles_communes = set(dico1.keys()) & set(dico2.keys())
<<<<<<<< HEAD:src/net_tools/compare_arp/compare.py
    repo = toml.load(conf)["repositories"]["net_tools_folder"] + "/ComparaisonARP"
    if os.path.exists(f"{repo}") is True:
        print("répertoire existant")
    else:
        os.system(f"mkdir {repo}")
    f = open(f"{repo}/Comparaison.md", "w")
========

    f = open(f"./src/CompareARP/Comparaison.md", "w")
>>>>>>>> master:src/CompareARP/compare.py
    f.write("| MAC @ | IP @ n°1 | IP @ n°2 | Changée ?" + "\r")
    f.write("| :---: | :---: | :---: | :---: |" + "\r")
    for cle in cles_communes:
        if list(dico1[cle].keys())[0] != list(dico2[cle].keys())[0]:
            f.write(f"| {cle} | {list(dico1[cle].keys())[0]} | {list(dico2[cle].keys())[0]} | {list(dico1[cle].keys())[0] != list(dico2[cle].keys())[0]}\r")
    f.close()


def main(site, table1, table2, conf):
    net_tools_folder = toml.load(conf)["repositories"]["net_tools_folder"]
    repo_json = net_tools_folder + "/GetARP/arp_tables/" + site + "/json/"
    t1 = repo_json + table1
    t2 = repo_json + table2
    dico1 = str_to_dico(t1)
    dico2 = str_to_dico(t2)
    compare_dicos(dico1,dico2, conf)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()