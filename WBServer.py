#Winged Boots server, by DaBoaz
<<<<<<< HEAD
#Version 0.15
=======
#Version 0.14
# -*- coding: utf-8 -*-
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff

from socket import *
import _thread as thread, sys  
from WBGui import *
from poly import *
<<<<<<< HEAD
from des import *
=======
from des import DES
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff

class WBServer():
	#send message to the client
	def send(self, msg):
		if msg[0] == '#':
			self.command(msg[1:])
			return
<<<<<<< HEAD
		if (self.cryptor != None):
			if (self.cryptor.mode != 'dec'): msg = self.cryptor.encrypt(msg)
		encodedMsg = msg.encode()
=======
		encodedMsg = msg.encode()
		if self.cryptor != None:
			if self.cryptor.mode != 'dec':
				encodedMsg = self.cryptor.encryptEncodedStr(encodedMsg)
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		connection.send(encodedMsg) #needed a mechanism to make sure msg < 1024 bytes
		
	#get message from the client
	def recvData(self):
		while True:
			data = connection.recv(1024)         
			if not data: break
<<<<<<< HEAD
			data = data.decode()
			if (self.cryptor != None):
				if (self.cryptor.mode != 'enc'): data = self.cryptor.decrypt(data)
			self.guiPrint(address[0]+' => '+data)
=======
			if self.cryptor != None:
				if self.cryptor.mode != 'enc':
					data = self.cryptor.decryptEncodedStr(data)
			self.guiPrint(address[0]+' => '+data.decode())
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		connection.close()
	
	#identifying encrypting commands
	def command(self, command):
		if command[:5] == "start":
			if command[6:10] == "poly":
				self.cryptor = poly()
				self.cryptor.mode = 'dual'
				self.cryptor.setKeys(command[11:])
			if command[6:9] == "des":
				self.cryptor = DES()
				self.cryptor.mode = 'dual'
<<<<<<< HEAD
				self.cryptor.setKeys(command[10:26])
			if command[6:10] == "3des":
				self.cryptor = TDES()
				self.cryptor.mode = 'dual'
				self.cryptor.setKeys(command[11:27], command[28:44], command[45:61])
=======
				self.cryptor.setKeys(command[10:])
>>>>>>> b6d0cc3ab53f6320791d9851c38e89c35f3a91ff
		if command[:7] == "encrypt":
			if command[8:12] == "poly":
				self.cryptor = poly()
				self.cryptor.mode = 'enc'
				self.cryptor.setEnKey(command[13:])
		if command[:7] == "decrypt":
			if command[8:12] == "poly":
				self.cryptor = poly()
				self.cryptor.mode = 'dec'
				self.cryptor.setDeKey(command[13:])
			
	#telling the gui to print	
	def guiPrint(self, message):
		self.message = message
		gui.event_generate("<<PrintMsg>>")
	
	#basic run of the server
	def run(self):
		myHost = ''                           
		myPort = 24766  
		
		self.cryptor = None #in charge of encrypting and decrypting
		
		sockobj = socket(AF_INET, SOCK_STREAM)       
		sockobj.bind((myHost, myPort))               
		sockobj.listen(5)
		global connection
		global address
		connection, address = sockobj.accept()
		global gui
		gui = WBGui(server=self)
		gui.printCon('Server connected by ' + str(address)+'\n')
		thread.start_new_thread(self.recvData, ())
		
		gui.mainloop()
	
if __name__ == "__main__":
	server = WBServer()
	server.run()