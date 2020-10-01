# メルカド・ニコアンヘロロペス

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

# generate key and IV----------------------------------------
# KEYSIZE = 32
# IVSIZE = 16

# key = os.urandom(KEYSIZE)
# iv = os.urandom(IVSIZE)

# file = open("key.bin", "wb")
# file2 = open("iv.bin", "wb")

# file.write(key)
# file2.write(iv)

# file.close()
# file2.close()
# -----------------------------------------------------------

# read generated key and IV---------------------------------
file = open("key.bin", "rb")
file2 = open("iv.bin", "rb")
key = file.read()
iv = file2.read()
file.close()
file2.close()
# -----------------------------------------------------------

# encyrptor-------------------------------------------------
file3 = open("encrypteddog.big", "rb")
data = file3.read()
data = data.ljust(len(data) + (32 - (len(data)%32)), b'0')
file3.close()
ALGO = algorithms.AES(key)
MODE = modes.CBC(iv)

cipher = Cipher(ALGO, MODE, backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(data) + encryptor.finalize()
file5 = open("encrypted.pdf", "wb")
file5.write(ct)
file5.close()
# -------------------------------------------------

# decryptor for checking -----------------------------------
decryptor = cipher.decryptor()
dt = decryptor.update(ct) + decryptor.finalize()

file4 = open("decrypted.pdf", "wb")
file4.write(dt)
file4.close()
# -------------------------------------------------------------