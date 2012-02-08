#Winged Boots DES encryptor/decryptor, by DaBoaz
<<<<<<< HEAD
#Version 0.15
=======
#Version 0.14
# -*- coding: utf-8 -*-
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff

class DES():
	def __init__(self):
		self.keys = None
		self.revK = None
		self.mode = None
		
	def encryptBlock(self, m, k): #k is an expanded key, m is in binary
		#encrypts 64bit block, return in bin
		if len(m) != 64: return("Error: wrong block size.")
		ip = self.IPing(m)
		l = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] #init 17 places
		r = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] #init 17 places
		l[0] = ip[:32]
		r[0] = ip[32:]
		for n in range(1,17):
			l[n] = r[n-1]
			f = self.theFunc(r[n-1], k[n])
			r[n] = self.xor(l[n-1], f)
		msg =  r[16] + l[16]
		reip = self.IPing(msg, r = True)
		return reip
		
<<<<<<< HEAD
	def encrypt(self, msg): #msg in string
		#encrypts string of any size
		msg = self.strToHex(msg)
=======
	def encrypt(self, msg): #msg in hex
		#encrypts hex string of any size
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		keys = self.keys 
		while len(msg)%16!=0: msg = '0' + msg
		m = self.hexToBin(msg) #msg is in hex
		encrypted = ''
		while len(m) > 64:
			encrypted += self.encryptBlock(m[:64], keys)
			m = m[64:]
		encrypted += self.encryptBlock(m, keys)
		encrypted = self.binToHex(encrypted)
		return encrypted #return in hex
		
<<<<<<< HEAD
=======
	def encryptEncodedStr(self, msg):#msg in bytes string
		msg = msg.decode()
		msg = self.strToHex(msg)
		encrypted = self.encrypt(msg)
		encrypted = encrypted.encode()
		return encrypted #encoded hex (byte string hex)
		
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
	def decrypt(self, cipher): #cipher in hex must be divisable by 16
		cipher = self.hexToBin(cipher)
		if len(cipher)%64 != 0: return "non DES Encrypted text"
		revK = self.revK
		plain = ''
		while len(cipher) > 64:
			plain = plain + self.encryptBlock(cipher[:64], revK)
			cipher = cipher[64:]
		plain += self.encryptBlock(cipher, revK)
		plain = self.binToHex(plain)
<<<<<<< HEAD
		plain = self.clean(plain) #removes the zeros in the begining
		return self.hexToStr(plain) #return in string
=======
		return plain #return in hex
		
	def decryptEncodedStr(self, cipher): #cipher in bytes string hex
		cipher = cipher.decode()
		plain = self.decrypt(cipher)
		plain = self.clean(plain)
		plain = self.hexToStr(plain)
		plain = plain.encode()
		return plain #return in encoded hex (bytes string hex)
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		
	def setKeys(self, k): #k in hex
		#set keys for decryption and encryption
		k = self.hexToBin(k)
		self.keys = self.keyExpanding(k)
		self.revK = self.reverseKeys(self.keys)	
	
	#internal methods for the des algorithm
	def reverseKeys(self, keys):
		newKeys = ['']*17
		for i in range(1, 17):
			newKeys[17-i] = keys[i]
		return newKeys
		
	def theFunc(self, r, k):
		expandedR = self.eBitSelection(r)
		xored = self.xor(k, expandedR)
		preFinal = self.SIng(xored)
		final = self.Ping(preFinal)
		return final

	def xor(self, a, b):
		if len(a) != len(b): return("Error, a and b are not in the same size.")
		#this is String 1' and 0' XOR!!!!!!!!
		out = ''
		for i in range(0, len(a)):
			if a[i] == b[i]: out = out + '0'
			else: out += '1'
		return out

	def eBitSelection(self, r):
		e = [32, 1, 2, 3, 4, 5,
			4, 5, 6, 7, 8, 9,
			8,  9, 10, 11, 12,  13,
			12, 13, 14, 15, 16, 17,
			16, 17, 18, 19, 20, 21,
			20, 21, 22, 23, 24, 25,
			24, 25, 26, 27, 28, 29,
			28, 29, 30, 31, 32, 1]
		ebit = self.tabeling(e, r)
		return ebit

	def SIng(self, b):
		s = ['', '', '', '', '', '', '', '', '']

		s[1]    =     [ [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7] ]
		s[1] = s[1] + [ [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8] ]
		s[1] = s[1] + [ [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0] ]
		s[1] = s[1] + [ [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13] ]

		s[2]    =     [ [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10] ]
		s[2] = s[2] + [ [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5] ]
		s[2] = s[2] + [ [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15] ]
		s[2] = s[2] + [ [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9] ]

		s[3]    =     [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8] ]
		s[3] = s[3] + [ [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1] ]
		s[3] = s[3] + [ [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7] ]
		s[3] = s[3] + [ [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12] ]

		s[4]    =     [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15] ]
		s[4] = s[4] + [ [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9] ]
		s[4] = s[4] + [ [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4] ]
		s[4] = s[4] + [ [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ]

		s[5]    =     [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9] ]
		s[5] = s[5] + [ [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6] ]
		s[5] = s[5] + [ [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14] ]
		s[5] = s[5] + [ [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3] ]

		s[6]    =     [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11] ]
		s[6] = s[6] + [ [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8] ]
		s[6] = s[6] + [ [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6] ]
		s[6] = s[6] + [ [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ]

		s[7]    =     [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1] ]
		s[7] = s[7] + [ [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6] ]
		s[7] = s[7] + [ [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2] ]
		s[7] = s[7] + [ [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ]

		s[8]    =     [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7] ]
		s[8] = s[8] + [ [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2] ]
		s[8] = s[8] + [ [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8] ]
		s[8] = s[8] + [ [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ]

		out = ''

		for n in range(1, 9):
			curr = b[6*(n-1):6*n]
			i = int((curr[0]+curr[5]), 2)
			j = int(curr[1:5], 2)
			toOut = bin(s[n][i][j])
			toOut = toOut[2:]
			while len(toOut) < 4: toOut = '0' + toOut
			out += toOut
		return out

	def Ping(self, b):
		p = [16, 7, 20, 21,
			29, 12, 28, 17,
			1, 15, 23, 26,
			5, 18, 31, 10,
			2, 8, 24, 14,
			32, 27, 3, 9,
			19, 13, 30, 6,
			22, 11, 4, 25]
		toReturn = self.tabeling(p, b)
		return toReturn

	def IPing(self, m, r = False):
		ip = [58,    50,   42,    34,    26,   18,    10,    2,
			60,    52,   44,    36,    28,   20,    12,    4,
			62,    54,   46,    38,    30,   22,    14,    6,
			64,    56,   48,    40,    32,   24,    16,    8,
			57,    49,   41,    33,    25,   17 ,    9,    1,
			59,    51,   43,    35,    27,   19,    11,    3,
			61,    53,   45,    37,    29,   21,    13,    5,
			63,    55,   47,    39,    31,   23,    15,    7]
		if r: return self.reverseTabeling(ip, m)
		return self.tabeling(ip, m)

	def keyExpanding(self, key): #key is 64bit string
		if len(key) != 64: return("Error: wrong key size.")
		kplus = self.pc1ing(key)
		cd = self.bitShiftingHandler(kplus)
		c = cd[0]
		d = cd[1]
		keys = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] #init 17 places (0-16, o is empty)
		for i in range(1, 17):
			keys[i] = self.pc2ing(c[i]+d[i])
		return keys

	def bitShift(self, bits):
		newBits = bits[1:]
		newBits += bits[0]
		return newBits

	def doubleBitShift(self, bits):
		return self.bitShift(self.bitShift(bits))

	def bitShiftingHandler(self, kplus):
		c = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] #init 17 places
		d = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] #init 17 places
		c[0] = kplus[:28]
		d[0] = kplus[28:]
		c[1] = self.bitShift(c[0])
		d[1] = self.bitShift(d[0])
		c[2] = self.bitShift(c[1])
		d[2] = self.bitShift(d[1])
		for i in range(3,9):
			c[i] = self.doubleBitShift(c[i-1])
			d[i] = self.doubleBitShift(d[i-1])
		c[9] = self.bitShift(c[8])
		d[9] = self.bitShift(d[8])
		for i in range(10,16):
			c[i] = self.doubleBitShift(c[i-1])
			d[i] = self.doubleBitShift(d[i-1])
		c[16] = self.bitShift(c[15])
		d[16] = self.bitShift(d[15])
		return (c, d)

	def tabeling(self, table, original):
		original = '0' + original #make the array start at [1] instaed of [0]
		final = ''
		for i in range(0, len(table)):
			final = final + original[table[i]]
		return final
		
	def reverseTabeling(self, table, original): 
		original = '0' + original #make the array start at [1] instaed of [0]
		final = ''
		toFinal = [''] + ['']*len(table)
		for i in range(0, len(table)):
			toFinal[table[i]] = original[i+1]
		for i in range(1, len(toFinal)): final = final + toFinal[i]
		return final

	def pc1ing(self, key):
		pc1 = [57, 49, 41, 33, 25, 17, 9,
			1, 58, 50, 42, 34, 26, 18,
			10, 2, 59, 51, 43, 35, 27,
			19, 11, 3, 60, 52, 44, 36,
			63, 55, 47, 39, 31, 23, 15,
			7, 62, 54, 46, 38, 30, 22,
			14, 6, 61, 53, 45, 37, 29,
			21, 13, 5, 28, 20, 12, 4]
		kplus = self.tabeling(pc1, key)
		return kplus

	def pc2ing(self, bits):
		pc2 = [14, 17, 11, 24, 1, 5,
			3, 28, 15, 6, 21, 10,
			23, 19, 12, 4, 26, 8,
			16, 7, 27, 20, 13, 2,
			41, 52, 31, 37, 47, 55,
			30, 40, 51, 45, 33, 48,
			44, 49, 39, 56, 34, 53,
			46, 42, 50, 36, 29, 32]
		k = self.tabeling(pc2, bits)
		return k
<<<<<<< HEAD
	
	def semiEncode(self, str):
		return [ord(i) for i in str]
	
	#few encoding methods:	
	def hexToBin(self, hex):
		bn = bin(int(hex, 16))[2:].zfill(len(hex)*4)
=======
		
	#few encoding methods:	
	def hexToBin(self, hex):
		bn = bin(int(hex, 16))[2:]
		while len(bn) != (len(hex)*4):
			bn = '0' + bn
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		return bn
		
	def binToHex(self, bin):
		hx = ''
<<<<<<< HEAD
		for i in range(0, len(bin), 4):	
			hx += hex(int(bin[i:i+4], 2))[2:]
		return hx
		
	def strToHex(self, str): #Str is normal string
		hx = ''
		str = self.semiEncode(str)
		for i in str:
			hx += hex(i)[2:].zfill(3)
		print(hx)
=======
		for i in range(0, int(len(bin)/4)):	
			hx += hex(int(bin[i*4:(i*4)+4], 2))[2:]
		return hx
		
	def strToHex(self, str):
		hx = ''
		if type(str) != type(b''): str = str.encode()
		for i in str:
			hx += hex(i)[2:]
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		return hx
	
	def hexToStr(self, hx):
		st = ''
<<<<<<< HEAD
		for i in range(0, len(hx), 3):
			st += chr(int(hx[i:i+3], 16))
		return st
		
	def clean(self, str): #can be bin or hex
		while str[0] == '0': str = str[1:]
		while len(str)%3!=0: str = '0' + str #make sure its diviseable by 3
		return str
		
class TDES(): #3DES, Triple DES
	#this class encrypts with the first key, and the decrypts with the 2nd key
	#and then encrypts with the 3rd key.
	def __init__(self):
		self.firstDES = DES()
		self.secondDES = DES()
		self.thirdDES = DES()
		
	def setKeys(self, key1, key2, key3): #keys in hex
		self.firstDES.setKeys(key1)
		self.secondDES.setKeys(key2)
		self.thirdDES.setKeys(key3)
		
	def encryptBlock(self, msg): #msg in binary
		if (len(msg) != 64): return("Error: wrong block size.")
		msg = self.firstDES.encryptBlock(msg, self.firstDES.keys)
		msg = self.secondDES.encryptBlock(msg, self.secondDES.revK)
		msg = self.thirdDES.encryptBlock(msg, self.thirdDES.keys)
		return msg #return binary value
		
	def decryptBlock(self, msg): #msg in binary
		if (len(msg) != 64): return("Error: wrong block size.")
		msg = self.thirdDES.encryptBlock(msg, self.thirdDES.revK)
		msg = self.secondDES.encryptBlock(msg, self.secondDES.keys)
		msg = self.firstDES.encryptBlock(msg, self.firstDES.revK)
		return msg #return binary value
		
	def encrypt(self, msg): #msg in string
		msg = self.firstDES.strToHex(msg)
		while len(msg)%16!=0: msg = '0' + msg
		m = self.firstDES.hexToBin(msg) #msg is in hex
		encrypted = ''
		while len(m) > 64:
			encrypted += self.encryptBlock(m[:64])
			m = m[64:]
		encrypted += self.encryptBlock(m)
		encrypted = self.firstDES.binToHex(encrypted)
		return encrypted #return in hex
		
	def decrypt(self, cipher): #plain in hex
		p = self.firstDES.hexToBin(cipher)
		plain = ''
		while len(p) > 64:
			plain += self.decryptBlock(p[:64])
			p = p[64:]
		plain += self.decryptBlock(p)
		plain = self.firstDES.binToHex(plain)
		plain = self.firstDES.clean(plain)
		print(plain,"   ",len(plain))
		plain = self.firstDES.hexToStr(plain)
		return plain #return in str
		

if __name__ == "__main__":
	tdes = TDES()
	tdes.setKeys('aaabaaabaaabaaab','0987098709870987', 'dfdfdf87dfdfdf87')
	a = "pizza"
	b = tdes.encrypt(a)
	print(b)
	c = tdes.decrypt(b)
	print(c)
	print(c == a)
=======
		for i in range(0, len(hx), 2):
			st += chr(int(hx[i:i+2], 16))
		return st
		
	def clean(self, bin): #can be bin or hex
		while bin[0] == '0': bin = bin[1:]
		return bin

if __name__ == "__main__":
	des = DES()
	a = 'pizza'
	print(des.strToHex(a))
	des.setKeys('ab78000a999c876a')
	c = '8374abc89283a902'
	d = des.encrypt(c)
	e = des.decrypt(d)
	print(e == c, e, d, c)
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
