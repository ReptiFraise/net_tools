Scripts d'analyse et de configuration du réseau
===============================================

Write ip adresses and names of routers in config.toml file

Output of script will be in the 'net_tools_folder'

Les scripts doivent être exécutés depuis le répertoire racine du dépôt git en lancant le script `Choice.py`.

Lorsque vous rajoutez une *adresse IP* et un *Nom de routeur* dans les fichiers au format `.txt`, le nom doit être positionnée sur la ligne portant le même numéro que celle sur laquelle est positionné l'adresse IP dans l'autre fichier.

Le répertoire `getARP` contient le script python qui permet de récupérer les tables ARP des routeurs PFSenses et les stock dans `getARP/arp_tables`, il retourne les tables dans le fichier `GetARP/Tables.md` pour être lisible.

Le répertoire `GetConfig` contient le script python qui permet de récupérer les configurations au format XML des routeurs dans le répertoire `GetConfig/conf_xml`.

Le répertoire `ExportNextCloud` contient le script `export.py` qui appelle le fichier `with_requests.py` qui prend en paramètre de sa fonction `upload()`, le chemin absolu du fichier à uploader. Le mot de passe de l'authentification HTTPS doit être stocké dans la variable d'environement `PASSWD`.

Le répertoire `CompareARP` permet d'exécuter le script qui compare 2 tables ARP d'un même routeur. Il retourne dans un tableau markdown les adresses MAC qui ont 2 adresses IP différentes entre 2 tables ARP. S'il n'y a aucune donnée dans le tableau après exécution, c'est que les 2 tables correspondent.



La structure du fichier config.toml, à placer dans le répertoire . relatif au script doit être:

[routers]
#IP addresses of routers
# Example :
# Router = "192.168.1.1"
RouterName = "x.x.x.x"


[repositories]
#list of repositories for data output
net_tools_folder = "repository for output"

[user]
#username for ssh connection, make sure that the username exist on remote
username = "username"
info = "info"
nextcloud = "nextcloud_username"