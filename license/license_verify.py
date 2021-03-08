import base64


from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from getmac import get_mac_address as gma
from win32crypt import CryptProtectData, CryptUnprotectData


PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
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


def decrypt(data):
    sypher = data
    # key = sypher[10:74]
    # sypher = sypher[:10] + sypher[74:]
    try:
        private_key = RSA.import_key(PRIVATE_KEY)
        cipher_rsa = PKCS1_OAEP.new(private_key)
        secret = cipher_rsa.decrypt(base64.b64decode(sypher)).decode()
        mac = u'' + gma()
        if mac == secret:
            return True
        else:
            return False
    except Exception:
        return False

def hash_license(data):
    return CryptProtectData(data)

def verify_license(data):
    try:
        if data:
            data = CryptUnprotectData(data)
            if decrypt(data[1]):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        return False

# verify_license()
# app = wx.App()
# frame = MyFrame()
# app.MainLoop()

# GM9DxwsU2zxrLX4ZZcxQUJKN3rud4r/rjIHoOSmSeUa9vi39kPvFjp5Vc6ccl3B9uxK2svko+tAvMUhuRvC1xkM7JCwBN6E9ZfLNI45QkWbpGrReL0i8bo48SV4f++S6wy8lPNlcLI0+ZXMdFeTsEBhH+/+uokRCaNCJbhgHNQs53TqPz8q3PnoB58SSravz7Wg7ojGEYJC6ewYxJuWqOJB6IKpNXnGohl0xIeVXyRP3s8Ywvc9tlGJMy1l+QFooYfTCOw+AWQ0nSRJ9VamPfaZlVKr/Px2hfUcQ6A/rx0jGQ3wyE1Wy2yQW8EezxW6uXX6Kh0fKNMLQvNkM9QIbrw==
# print(decrypt("dTGSxtzYbQOpHTgIcKYST0Hu4bpeErjV83U4tfGxrI8TOD3D/Vw7TzYsJyX57DfRFG1d6LOaiLvmMIB/bUnVU/wCnS99VpfXYl267uCi+CVn7A3ryAgK9QeKg1bv3eS3OU2S9NoCkggUWdZyxIyoffB+ge8yOKKlr2hjYt6qPnY/BlsSQ92DiESfB4e+u5uWqE6BTJKrmzpuJgYYB92tscd+lG2PWkcrFWAynwgNRCLD7fzIbXQJ+eo4gM476SWcgqfay8hfHFHjj7fs5ucsrGA7zwqFV5a+YoS5bukbMSqonWGx0FPdYV4M8QgZjLqGgLtnGrCmdHGorBmBSeqIbg=="))
