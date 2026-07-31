import json
import os
import zipfile
import hashlib
import requests

JAR_URL = 'https://piston-data.mojang.com/v1/objects/ba2df812c2d12e0219c489c4cd9a5e1f0760f5bd/client.jar'
JAR_SHA1 = 'ba2df812c2d12e0219c489c4cd9a5e1f0760f5bd'
JAR_PATH = 'client_1.21.11.jar'
OUTPUT_ZIP = 'vanilla_1.21.11_full.zip'
TEXTURE_PREFIX = 'assets/minecraft/textures/'

def download_jar():
    if os.path.exists(JAR_PATH):
        with open(JAR_PATH, 'rb') as f:
            sha1 = hashlib.sha1(f.read()).hexdigest()
        if sha1 == JAR_SHA1:
            print(f'Client jar already exists and sha1 matches: {JAR_PATH}')
            return
        else:
            print('Existing jar sha1 mismatch, re-downloading...')

    print(f'Downloading client jar from {JAR_URL}...')
    resp = requests.get(JAR_URL, stream=True, timeout=60)
    resp.raise_for_status()
    with open(JAR_PATH, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

    with open(JAR_PATH, 'rb') as f:
        sha1 = hashlib.sha1(f.read()).hexdigest()
    if sha1 != JAR_SHA1:
        raise ValueError(f'Downloaded jar sha1 mismatch: {sha1}')
    print(f'Downloaded and verified: {JAR_PATH}')

def extract_textures():
    extracted = 0
    with zipfile.ZipFile(JAR_PATH, 'r') as jar:
        with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as out:
            for name in jar.namelist():
                if name.startswith(TEXTURE_PREFIX) and name.lower().endswith('.png'):
                    data = jar.read(name)
                    out.writestr(name, data)
                    extracted += 1

            out.writestr('pack.mcmeta', json.dumps({
                "pack": {
                    "pack_format": 55,
                    "description": "Minecraft 1.21.11 Vanilla Textures extracted from client.jar"
                }
            }, indent=2))

    print(f'Extracted {extracted} textures to {OUTPUT_ZIP}')

if __name__ == '__main__':
    download_jar()
    extract_textures()
