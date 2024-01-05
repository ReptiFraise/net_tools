"""
This code is made for execute the command tcpdump on interfaces WAN,LAN,OPNVPN of the pfSenses firewalls
The script needs a gpg file that contains the passwords of admin accounts of firewalls to execute the tcpdump command
The dumps are downloaded on local folder with the name of router and name of the interface
"""

import gnupg
import json
from getpass import getpass
import paramiko

def decrypt_gpg_file(file_path, gpg_home_path):
    gpg = gnupg.GPG(gnupghome=gpg_home_path)

    with open(file_path, 'rb') as f:
        #passphrase = getpass()
        decrypted_data = gpg.decrypt_file(f, passphrase='WLRpm9NGyoKZDeNK3Juiswh7', output=None, always_trust=True)
    
    return decrypted_data.data.decode('utf-8')


def parse_json_data(json_string):
    return json.loads(json_string)

def tcpdump(passwd):
    password = passwd['Freyming']
    host = "10.57.2.254"
    port = 8022
    username = "admin"
    try:
        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()
        # Automatically add the server's host key (this is insecure, use it only for testing purposes)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to the remote server
        ssh_client.connect(hostname=host, port=port, username=username, password=password)
        # Execute a command remotely
        command = 'ls -l /home/alban'
        stdin, stdout, stderr = ssh_client.exec_command(command)
        # Read the output of the command
        print("Command Output:")
        print(stdout.read().decode())
        # Close the SSH connection
        ssh_client.close()
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH error: {e}")
    except paramiko.BadHostKeyException as e:
        print(f"Host key error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main(conf):
    file_path = "/home/alban/ADMINS_PASSWD.json.gpg"
    gpg_home_path = "/home/alban/.gnupg"

    decrypted_json_string = decrypt_gpg_file(file_path, gpg_home_path)
    decrypted_data_dict = parse_json_data(decrypted_json_string)
    print(tcpdump(decrypted_data_dict))