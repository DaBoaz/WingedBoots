#Winged Boots polyalphabetic encryptor/decryptor, by DaBoaz
#Version 0.14
# -*- coding: utf-8 -*-


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

	def encryptEncodedStr(self, plaintext):
		#encrypts. plaintext must be in byte-string, returns byte-string
		ciphertext = ""
		key = self.encryptKey
		for i in range(0, len(plaintext)):
			keyi = i%len(key)
			letNum = plaintext[i]^key[keyi]
			ciphertext += chr(letNum)
		return ciphertext.encode()
		
	def decryptEncodedStr(self, ciphertext):
		#decrypts. ciphertext must be in byte-string, returns byte-string
		plaintext = ""
		key = self.decryptKey
		for i in range(0, len(ciphertext)):
			keyi = i%len(key)
			letNum = ciphertext[i]^key[keyi]
			plaintext += chr(letNum)
		return plaintext.encode()
		
if __name__ == "__main__":
	cyp = poly()
	cyp.setEnKey("ik")
	cyp.setDeKey("ik")
	msg = b"UncleJohnsBand"
	ci = cyp.encryptEncodedStr(msg)
	print(ci)
	print(ci.decode())
	pi = cyp.encryptEncodedStr(ci)
	print(pi)