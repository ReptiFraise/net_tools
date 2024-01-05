import pkgutil
import pyfiglet
from pathlib import Path
from net_tools.get_arp.main import main as getARP
from net_tools.get_config.main import main as getConfig
from net_tools.export_nextcloud.main import main as exportNextCloud
from net_tools.compare_arp.main import main as compareARP
from net_tools.packet_capture.main import main as packetCapture


def print_large_text(text):
    ascii_banner = pyfiglet.figlet_format(text, font="big")
    print(ascii_banner)


def choix():
    phrase = "| Choisissez le script que vous voulez lancer : |"
    print("*" * len(phrase))
    print(phrase)
    print("*" * len(phrase))
    scripts = ["GetARP", "GetConfig", "ExportNextCloud", "CompareARP", "ExportConfig", "PacketCapture", "Exit"]

    for i in range(len(scripts)):
        print(f"{i} : {scripts[i]}")
    val = 0
    while True:
        choix = input("--> : ")
        try:
            val = int(choix)
            if val in range(0, len(scripts)):
                print("OK")
                break
            else:
                print("Il faut entrer le numéro d'un script")
                continue
        except ValueError:
            print("Il faut entrer le numéro d'un script")
            continue
    return scripts[val]


def appel_script(name, conf):
    match name:
        case "GetARP":
            getARP(conf)
        case "GetConfig":
            getConfig(conf)
        case "ExportNextCloud":
            exportNextCloud(conf)
        case "CompareARP":
            compareARP(conf)
        case "PacketCapture":
            packetCapture(conf)
        case "Exit":
            conf = conf
            exit()


def main():
    print_large_text("net tools")
    conf_file = Path("./config.toml")
    try:
        print("./config.toml will be used")
        appel_script(choix(), conf=conf_file)
    except:
        print("./config.toml doesn't exist, the file will be created from default configuration file of the package")
        conf_file = pkgutil.get_data(__name__, "./resources/config.toml").decode("utf-8")
        with open('config.toml', 'w') as file:
            file.write(conf_file)
            file.close()
        config = "config.toml"
        appel_script(choix(), conf=config)