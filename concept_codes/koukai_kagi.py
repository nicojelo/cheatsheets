# Author: Mercado Nico Angelo Lopez
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def genKeyPair():
	# generate pair
	private_key = rsa.generate_private_key(
	    public_exponent=65537,
	    key_size=2048,
	    backend=default_backend()
	)
	public_key = private_key.public_key()

	# save to file

	pem = private_key.private_bytes(
	    encoding=serialization.Encoding.PEM,
	    format=serialization.PrivateFormat.PKCS8,
	    encryption_algorithm=serialization.NoEncryption()
	)

	with open('private_key.pem', 'wb') as f:
	    f.write(pem)

	pem = public_key.public_bytes(
	    encoding=serialization.Encoding.PEM,
	    format=serialization.PublicFormat.SubjectPublicKeyInfo
	)

	with open('public_key.pem', 'wb') as f:
	    f.write(pem)

def decrypt(privatekeyFile, filetoDecrypt):
	with open(privatekeyFile, "rb") as key_file:
	    private_key = serialization.load_pem_private_key(
	        key_file.read(),
	        password=None,
	        backend=default_backend()
	    )
	with open(filetoDecrypt, "rb") as data_file:
		data = data_file.read()

	decrypted = private_key.decrypt(
	    data,
	    padding.OAEP(
	        mgf=padding.MGF1(algorithm=hashes.SHA256()),
	        algorithm=hashes.SHA256(),
	        label=None
	    )
	)

	f = open("decrypted.bin", "wb")
	f.write(decrypted)
	f.close()

def encrypt(publickeyFile, fileToEncrypt):
	with open(publickeyFile, "rb") as key_file:
	    public_key = serialization.load_pem_public_key(
	        key_file.read(),
	        backend=default_backend()
	    )
	with open(fileToEncrypt, "rb") as data_file:
		data = data_file.read()

	encrypted = public_key.encrypt(
	    data,
	    padding.OAEP(
	        mgf=padding.MGF1(algorithm=hashes.SHA256()),
	        algorithm=hashes.SHA256(),
	        label=None
	    )
	)

	f = open("encrypted.bin", "wb")
	f.write(encrypted)
	f.close()


if __name__ == '__main__':
	if(sys.argv[1] == "-g"):
		genKeyPair()
	elif(sys.argv[1] == "-d"):
		decrypt(sys.argv[2], sys.argv[3])
	elif(sys.argv[1] == "-e"):
		encrypt(sys.argv[2], sys.argv[3])
	else:
		print("使い方")
		print("\n Generate Key Pairs: python3 -g")
		print("\n Decrypt: python3 -d <privatekey file> <file to decrypt>")
		print("\n NOTE --- decrypted file is named [decrypted.bin]")
		print("\n Encrypt: python3 -e <publickey file> <file to encrypt>")
		print("\n NOTE --- encrypted file is named [encrypted.bin]")