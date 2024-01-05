import os
import toml
import net_tools.compare_arp.main   as compare
import net_tools.__main__ as net_tools
def choix_repo(conf):
    phrase = "| Choisissez le Site pour lequel vous voulez comparer les tables ARP |"
    print("*" * len(phrase))
    print(phrase)
    print("*" * len(phrase))
    net_tools_repo = toml.load(conf)["repositories"]["net_tools_folder"]
    repos = os.listdir(f"{net_tools_repo}/GetARP/arp_tables")
    repos = os.listdir("./src/GetARP/Tables_json")
    for i in range(len(repos)):
        print(f"{i} : {repos[i]}")

    while True:
        choix = (input("--> : "))
        try:
            val = int(choix)
            if val in range(0,len(repos)) :
                print("OK")
                break
            else:
                print("Il faut entrer le numéro d'un répertoire")
                continue
        except ValueError:
            print("Il faut entrer le numéro d'un répertoire")
            continue
    return repos[int(choix)]


def choix_tables(repo, conf):
    net_tools_folder = toml.load(conf)["repositories"]["net_tools_folder"]
    tables = os.listdir(f"{net_tools_folder}/GetARP/arp_tables/{repo}/json")
def choix_tables(repo):
    tables = os.listdir(f"src/GetARP/Tables_json/{repo}")
    phrase = "| Choisissez les 2 tables ARP que vous voulez comparer |"
    print("*" * len(phrase))
    print(phrase)
    print("*" * len(phrase))

    for i in range(len(tables)):
        print(f"{i} : {tables[i]}")
    tables_choisies = []
    print("Table n°1 à comparer")
    while True:
        choix = (input("--> : "))
        try:
            val = int(choix)
            if val in range(0,len(tables)) :
                print("OK")
                tables_choisies.append(tables[val])
                break
            else:
                print("Il faut entrer le numéro d'une table")
                continue
        except ValueError:
            print("Il faut entrer le numéro d'une table")
            continue
    print("Table n°2 à comparer")
    while True:
        choix = (input("--> : "))
        try:
            val = int(choix)
            if val in range(0,len(tables)) :
                print("OK")
                tables_choisies.append(tables[val])
                break
            else:
                print("Il faut entrer le numéro d'une table")
                continue
        except ValueError:
            print("Il faut entrer le numéro d'une table")
            continue
    print(f"\nLes tables {tables_choisies[0]} et {tables_choisies[1]} vont être comparées")
    print(f"Le résultat se trouve dans {net_tools_folder}/CompareARP/Comparaison.md")
    print("Le résultat se trouve dans Comparaison.md")
    compare.main(repo, tables_choisies[0], tables_choisies[1])


def main(conf):
    repo = choix_repo(conf)
    choix_tables(repo, conf)
    net_tools.main()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()