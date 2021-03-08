from Crypto.PublicKey import RSA
import random
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
from getmac import get_mac_address as gma
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoQesYTU9LgmL2e4II8If
7dWw20tWg0rdJuHMrG64GEPZi+vI1dX2rcsGprcgI2FHqQ8mdmRbf2F2asJRe9Na
ST+UqEcatnbpCFBdmrIF90VklavtFYZoz0d1AG+RtF83+Ks/klu0BvV37gQC+Uy+
N8zjF6c/+hADUN3YXkf5Nl/8JKPYlJeDQJzx4fa4Pbr88kbq87GdA4IE5DhEwbyT
dWQGZDJ/agX3rIrrEblichjSu/ueK4gHK/4oNRpPYHeBRbPMLoPy4uxTB0KLBHTz
hMKhtXRKBzhqUs/gJ0BXtnL4KEORvjY4XnycNLOPkd5X5A5ubAWQBbvMyzbYs8+s
DwIDAQAB
-----END PUBLIC KEY-----"""


def encrypt(data):
    # secret = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=64))
    # data = (date+','+secret).encode("utf-8")
    recipient_key = RSA.import_key(PUBLIC_KEY)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    cypher = cipher_rsa.encrypt(data)
    text = base64.b64encode(cypher).decode()
    # text = text[:10] + secret + text[10:]
    return text

if __name__ == '__main__':
    print("welcome to SharpMap licence generator")
    mac=raw_input("Please Enter mac address you want to license")
    while not mac:
        mac = raw_input("Please Enter a valid mac address you want to license")
    print("Your license is")
    print("------------------------------------------------------")
    print(encrypt(mac.lower()))
    print("------------------------------------------------------")
    mac = raw_input("press any key to exit")