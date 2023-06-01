import base64
import json

def base64url_encode(value):
    return base64.urlsafe_b64encode(value).rstrip(b"=")

header={"typ": "JWT", "alg": "NONE"}
payload={"id": "nguyenanhnam", "username": "nemnem", "year": "1945"}

b64header = base64url_encode(json.dumps(header).encode())
b64payload = base64url_encode(json.dumps(payload).encode())

# Phần Sign chúng ta có thể để tùy chỉnh như nào cũng được
token = b".".join([b64header,b64payload,base64url_encode(b"MSEC_TEAM")]).decode()
print(f"{token=}")