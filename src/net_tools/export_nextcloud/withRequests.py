import os
import toml
import requests
import getpass
import urllib.parse

def upload(file_name,conf):
    nextcloud_url = "https://cloud.vizyon.ai/nextcloud/remote.php/webdav"
    username = toml.load(conf)["user"]["nextcloud"]
    password = getpass.getpass("Password: ")
    file_to_upload = f"{file_name}"
    session = requests.Session()
    session.auth = (username, password)
    with open(file_to_upload, "rb") as file:
        file_content = file.read()
    file_name = file_name.split('/')[-1]
    print(file_name)
    upload_url = nextcloud_url + f'/BACKUP/{file_name}'
    print(upload_url)
    response = session.put(upload_url, data=file_content)
    if response.status_code == 200 or response.status_code == 201:
        print("File uploaded successfully.")
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")