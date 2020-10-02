# メルカド・ニコアンヘロロペス

import os
import sys

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()

def pad(m):
	return+char

def generateKey(keyFileName, ivFileName):
	KEYSIZE = 32
	IVSIZE = 16

	key = os.urandom(KEYSIZE)
	iv = os.urandom(IVSIZE)

	fileok = open(keyFileName, "wb")
	fileoi = open(ivFileName, "wb")

	fileok.write(key)
	fileoi.write(iv)

	fileok.close()
	fileoi.close()

def encrypt(keyFileName, ivFileName, dataFileName):
	# read key and iv
	fileok = open(keyFileName, "rb")
	fileoi = open(ivFileName, "rb")
	key = fileok.read()
	iv = fileoi.read()
	fileok.close()
	fileoi.close()

	# read data
	fileod = open(dataFileName, "rb")
	data = fileod.read()
	data = data.ljust(len(data) + (32 - (len(data)%32)), b'0')
	fileod.close()

	# encrypt
	ALGO = algorithms.AES(key)
	MODE = modes.CBC(iv)
	cipher = Cipher(ALGO, MODE, backend=backend)
	encryptor = cipher.encryptor()
	ct = encryptor.update(data) + encryptor.finalize()
	
	# output
	fileoo = open("encrypted.bin", "wb")
	fileoo.write(ct)
	fileoo.close()

def decrypt(keyFileName, ivFileName, dataFileName):
	# read key and iv
	fileok = open(keyFileName, "rb")
	fileoi = open(ivFileName, "rb")
	key = fileok.read()
	iv = fileoi.read()
	fileok.close()
	fileoi.close()

	# read data
	fileod = open(dataFileName, "rb")
	data = fileod.read()
	# data = data.ljust(len(data) + (32 - (len(data)%32)), b'0')
	fileod.close()

	# decrypt
	ALGO = algorithms.AES(key)
	MODE = modes.CBC(iv)
	cipher = Cipher(ALGO, MODE, backend=backend)
	decryptor = cipher.decryptor()
	dt = decryptor.update(data) + decryptor.finalize()
	dt = dt.rstrip(b'0')

	# output 
	fileoo = open("decrypted.bin", "wb")
	fileoo.write(dt)
	fileoo.close()
# -------------------------------------------------------------

if __name__ == '__main__':
	if(sys.argv[1] == "-g"):
		generateKey(sys.argv[2], sys.argv[3])
	elif(sys.argv[1] == "-e"):
		encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
	elif(sys.argv[1] == "-d"):
		decrypt(sys.argv[2], sys.argv[3], sys.argv[4])