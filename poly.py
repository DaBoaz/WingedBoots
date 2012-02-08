#Winged Boots polyalphabetic encryptor/decryptor, by DaBoaz
<<<<<<< HEAD
#Version 0.15
=======
#Version 0.14
# -*- coding: utf-8 -*-
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff


#note that this function is used for both encryption and decryption

class poly():
	def __init__(self):
	#Setting the keys
		self.encryptKey = None
		self.decryptKey = None
		self.mode = None
	
	def setEnKey(self, inputKey):
	#setting encryption key only
		self.encryptKey = inputKey.encode()
		
	def setDeKey(self, inputKey):
	#setting decryption key only
		self.decryptKey = inputKey.encode()
		
	def setKeys(self, key):
	#setting both keys
		self.encryptKey = key.encode()
		self.decryptKey = key.encode()

<<<<<<< HEAD
	def encrypt(self, plaintext):
		#encrypts. plaintext must be in string, returns string
		plaintext = self.semiEncode(plaintext)
=======
	def encryptEncodedStr(self, plaintext):
		#encrypts. plaintext must be in byte-string, returns byte-string
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		ciphertext = ""
		key = self.encryptKey
		for i in range(0, len(plaintext)):
			keyi = i%len(key)
			letNum = plaintext[i]^key[keyi]
			ciphertext += chr(letNum)
<<<<<<< HEAD
		return ciphertext
		
	def decrypt(self, ciphertext):
		#decrypts. ciphertext must be in string, returns string
		ciphertext = self.semiEncode(ciphertext)
=======
		return ciphertext.encode()
		
	def decryptEncodedStr(self, ciphertext):
		#decrypts. ciphertext must be in byte-string, returns byte-string
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		plaintext = ""
		key = self.decryptKey
		for i in range(0, len(ciphertext)):
			keyi = i%len(key)
			letNum = ciphertext[i]^key[keyi]
			plaintext += chr(letNum)
<<<<<<< HEAD
		return plaintext
		
	def semiEncode(self, str):
		return [ord(i) for i in str]
=======
		return plaintext.encode()
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		
if __name__ == "__main__":
	cyp = poly()
	cyp.setEnKey("ik")
	cyp.setDeKey("ik")
<<<<<<< HEAD
	msg = "UncleJohnsBand"
	ci = cyp.encrypt(msg)
	print(ci)
	pi = cyp.encrypt(ci)
	print(pi)
	print(pi == msg)
=======
	msg = b"UncleJohnsBand"
	ci = cyp.encryptEncodedStr(msg)
	print(ci)
	print(ci.decode())
	pi = cyp.encryptEncodedStr(ci)
	print(pi)
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
