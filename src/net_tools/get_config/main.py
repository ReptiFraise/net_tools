import toml
from .getConfig import main as get_config_main
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


def choice_router(Sites):
    """
    Choisis le routeur sur lequel on récupère le fichier config.xml
    :return: Le numéro d'index du Site dans la liste Sites
    """
    phrase = "| Choisissez le routeur sur lequel vous voulez récupérer le fichier config.xml |"
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
            "Vous avez choisis de récupérer les fichiers config.xml de tous les "
            "routeurs PfSense."
        )
        for i in range(len(IP)):
            get_config_main(Sites[i], IP[i], conf)
    else:
        print(
            f"Vous allez récupérer le fichier config.xml du Site de {Sites[choix]} qui "
            f"a pour adresse IP {IP[choix]}."
        )
        get_config_main(Sites[choix], IP[choix], conf)
    net_tools.main()