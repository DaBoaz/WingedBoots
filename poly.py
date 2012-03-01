#Winged Boots polyalphabetic encryptor/decryptor, by DaBoaz
#Version 0.16


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

	def encrypt(self, plaintext):
		#encrypts. plaintext must be in string, returns string
		plaintext = self.semiEncode(plaintext)
		ciphertext = ""
		key = self.encryptKey
		for i in range(0, len(plaintext)):
			keyi = i%len(key)
			letNum = plaintext[i]^key[keyi]
			ciphertext += chr(letNum)
		return ciphertext
		
	def decrypt(self, ciphertext):
		#decrypts. ciphertext must be in string, returns string
		ciphertext = self.semiEncode(ciphertext)
		plaintext = ""
		key = self.decryptKey
		for i in range(0, len(ciphertext)):
			keyi = i%len(key)
			letNum = ciphertext[i]^key[keyi]
			plaintext += chr(letNum)
		return plaintext
		
	def semiEncode(self, str):
		return [ord(i) for i in str]
		
if __name__ == "__main__":
	cyp = poly()
	cyp.setEnKey("ik")
	cyp.setDeKey("ik")
	msg = "UncleJohnsBand"
	ci = cyp.encrypt(msg)
	print(ci)
	pi = cyp.encrypt(ci)
	print(pi)
	print(pi == msg)