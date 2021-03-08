from Crypto.PublicKey import RSA
import random
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import string
from datetime import datetime

from win32con import HKEY_LOCAL_MACHINE
from win32crypt import CryptProtectData,CryptUnprotectData
from win32api import RegCreateKey

PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoQesYTU9LgmL2e4II8If
7dWw20tWg0rdJuHMrG64GEPZi+vI1dX2rcsGprcgI2FHqQ8mdmRbf2F2asJRe9Na
ST+UqEcatnbpCFBdmrIF90VklavtFYZoz0d1AG+RtF83+Ks/klu0BvV37gQC+Uy+
N8zjF6c/+hADUN3YXkf5Nl/8JKPYlJeDQJzx4fa4Pbr88kbq87GdA4IE5DhEwbyT
dWQGZDJ/agX3rIrrEblichjSu/ueK4gHK/4oNRpPYHeBRbPMLoPy4uxTB0KLBHTz
hMKhtXRKBzhqUs/gJ0BXtnL4KEORvjY4XnycNLOPkd5X5A5ubAWQBbvMyzbYs8+s
DwIDAQAB
-----END PUBLIC KEY-----"""

PRIVATE_KEY="""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAoQesYTU9LgmL2e4II8If7dWw20tWg0rdJuHMrG64GEPZi+vI
1dX2rcsGprcgI2FHqQ8mdmRbf2F2asJRe9NaST+UqEcatnbpCFBdmrIF90Vklavt
FYZoz0d1AG+RtF83+Ks/klu0BvV37gQC+Uy+N8zjF6c/+hADUN3YXkf5Nl/8JKPY
lJeDQJzx4fa4Pbr88kbq87GdA4IE5DhEwbyTdWQGZDJ/agX3rIrrEblichjSu/ue
K4gHK/4oNRpPYHeBRbPMLoPy4uxTB0KLBHTzhMKhtXRKBzhqUs/gJ0BXtnL4KEOR
vjY4XnycNLOPkd5X5A5ubAWQBbvMyzbYs8+sDwIDAQABAoIBAAqXDJkf/TQH4LCm
XNatL5hek1D4tWnRBJZIB0PXzDecTrRK/1xAxAZN8dQI+w4YmbPekTL8CqBn8ne2
69Du52Ml0Ur30iPp0g1/64f+6TGH2MOXGPJvcnkfQ+yRac2o7W9nI7kmWsKSZh67
GM74YxIcYVru3uA9KVqqHE6nARa4Qmd2NxsDt4b/oYAHJFvLJ1vzWWk7SeStvGDA
JD7nUSRENRgLYfMbg3ZIeCMZC6X08SB+wjv0rr0j+ZGhinFUl1wFO780Z926mV3/
6grH+/vtIYymLwJMYeOZX8HWKces5vWTVAcPijCay2E0b9djULMz17pfBS6zHwVt
+ytkSdECgYEAtZFJ6gGEGyDxZPy0TOEgkksk7mG6j9Gk42wAXIGyIzF7lXqJ9HHk
jvhMavyAtvmpVB1FWjklqPGDtlrKFN9sTYYh1e8Fjdeo7RVv/7rHMJog/T1ebWQE
nLBkb5gXE+dNp2ZQdIWShjCcoiM9PFQB9MAWWPUH08dMyzNktWQtKesCgYEA4wsO
8IVdnthTQdacFeTE/rkHS8VcbzOMhqccaCDxXtPOOccPp+z+7NCFZSR5uW21hLY9
aLr41pOmWy/HX8DkrAzAL7fSjkHhcoBMbHqev3oRVuj0gE5rgZuSzG75DrfSXCIn
w2Pn7ZE/IaBhtjUAYGCj7DsTJQlQnJX6us9euW0CgYAGH2ogrABqccfyIdtqpETW
6hXKvBzwcJ9g0+mHNRBuw2JpfgJc7eJJN/JLwUwN34loPrxx+G9erRZF9fXOkmIy
kw1dC3xidh1KMWjfdMr2xpvKLmGayr6lEgWxBa3xi+FAfeDErSRtxgHiLdII0MRo
HnoicdDbwWLDj24b987WFQKBgBSKRpK57gtV1MprCPnuFWhaAu/27fLdfgQckDRX
bp6+mLSfbqophbKU9sx8rUp6Q2a7OfkEmUiIWQ981hOylr199dEbV0Apc6TxOHjD
6yK1f2YWczA8Z/t0wKYgEAYl2TEeoexKWIwkjMqVAOIED4GonIvdmFDMc++GngVS
h2ZNAoGAZlLxar9kjFroiSJV/yqbyGRBHiP7Krbm9/n23QhudYm3zDXx4p0ZAhii
8ZIsr+L8GWUSZqfxcihppWMuaSm/QRa03Fn/e9D9fkE2TlyLzo75z2EG0ZWzlCOe
2Mbp01GIuUXTpCYL8u3JjBE4XiXqo2MV76CAGs/12eyl+Z1aH/E=
-----END RSA PRIVATE KEY-----"""

def rsakeys():
    key = RSA.generate(2048)
    publickey = key.publickey()
    with open("public.pem", mode="wb") as publicFile, open("private.pem", mode="wb") as privateFile:
        publicFile.write(publickey.publickey().exportKey())
        privateFile.write(key.exportKey())
    return key, publickey




