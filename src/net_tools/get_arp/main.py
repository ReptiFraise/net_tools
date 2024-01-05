import toml
from net_tools.get_arp.getTable import main as get_table_main
import net_tools.__main__ as net_tools


def init(conf):
    Sites = []
    IP = []
    data = toml.load(conf)
    for cle in data["routers"]:
        IP.append(data["routers"][cle])
        Sites.append(cle)

    Sites_builder = []
    IP_builder = []
    for site in Sites:
        Sites_builder.append(site.strip())
    for ip in IP:
        IP_builder.append(ip.strip())

    Sites = Sites_builder
    IP = IP_builder
    return (Sites, IP)


def get_tables(Sites, IP, conf):
    for i in range(len(Sites)):
        if Sites[i] != "Tous les routeurs":
            ip = IP[i].strip()
            name = Sites[i].strip()
            print(ip + " // " + name)
            get_table_main(name, ip, conf)


def choice_router(Sites):
    """
    Choisis le routeur sur lequel on récupère la table ARP
    :return: Le numéro d'index du Site dans la liste Sites
    """
    phrase = "| Choisissez le routeur sur lequel vous voulez récupérer la table ARP |"
    print("*" * len(phrase))
    print(phrase)
    print("*" * len(phrase))
    Sites.append("Tous les routeurs")
    for i in range(len(Sites)):
        if i < 10:
            print(f" {i} : {Sites[i]}")
        else:
            print(f"{i} : {Sites[i]}")

    while True:
        choix = input("--> : ")
        try:
            val = int(choix)
            if val in range(0, len(Sites)):
                print("OK")
                res = val
                break
            else:
                print("Il faut entrer le numéro d'un Site")
                continue
        except ValueError:
            print("Il faut entrer le numéro d'un Site")
            continue
    return res


def main(conf):
    Sites, IP = init(conf)
    choix = choice_router(Sites)
    if Sites[choix] == "Tous les routeurs":
        print(
            "Vous avez choisis de récupérer les tables ARP de tous les "
            "routeurs PfSense."
        )
        get_tables(Sites, IP, conf)
    else:
        print(
            f"Vous allez récupérer la table ARP du Site de {Sites[choix]} qui "
            f"a pour adresse IP {IP[choix]}."
        )
        print(toml.load(conf))
        get_table_main(Sites[choix], IP[choix], conf)
        
    net_tools.main()