from base64 import b64encode, b64decode
import hashlib
import random
import json


data_cookie = "eyJ1c2VybmFtZSI6ICJuZW1uZW0iLCAidXNlcl90eXBlIjogImJhc2ljIn0="
hash_cookie = "f67f32d22ecad24aa1ef33aaa47f174218e6d399abd0fc50205a6d8905807c7f"
username = "nemnem"

def hash(data):
    return hashlib.sha256(bytes(data, 'utf-8')).hexdigest()

def find_key():
    data = {"username": username,"user_type": "basic"}
    
    for i in range(0xFFFFFF):
        key = hex(i)[2:]
        b64data = b64encode(json.dumps(data).encode())
        data_hash = hash(b64data.decode() + key)
        if b64data.decode() == data_cookie and data_hash == hash_cookie:
            print("Found key: "+key)
            exit(0)
        if i % 1000000 == 0:
            print(f"{i=}")

def change_data(key_found):
    data = {"username": username,"user_type": "premium"}
    b64data = b64encode(json.dumps(data).encode())
    data_hash = hash(b64data.decode() + key_found)
    print(f"{b64data=},{data_hash=}")

find_key()
#change_data('73d18e')