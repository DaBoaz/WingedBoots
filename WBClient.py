#Winged Boots client, by DaBoaz
#Version 0.16

import sys, _thread as thread
from socket import *
from tkinter import *
from WBGui import *
from poly import *
from des import *
from aes import *

class WBClient():
	#Getting Information from the server.
	def listen(self, sockobj, name):
		while True:
			msg = sockobj.recv(1024)
			if not msg: break
			msg = msg.decode()
			if (self.cryptor != None):
				if (self.cryptor.mode!= 'enc'): msg = self.cryptor.decrypt(msg)
			self.guiPrint(name+' => '+msg)
			
	#sends message to the server	
	def send(self, msg):
		if msg[0] == '#':
			self.command(msg[1:])
			return
		if (self.cryptor != None ):
			if (self.cryptor.mode!= 'dec'): msg = self.cryptor.encrypt(msg)
		sockobj.send(msg.encode())
	
	#telling the gui to print message
	def guiPrint(self, message):
		self.message = message
		gui.event_generate("<<PrintMsg>>")

	#used to get the server address from the popup
	def fetch(self, event):
		self.serverHost = ent.get()
		root.destroy()
		
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
				self.cryptor.setKeys(command[10:26])
			if command[6:10] == "3des":
				self.cryptor = TDES()
				self.cryptor.mode = 'dual'
				self.cryptor.setKeys(command[11:27], command[28:44], command[45:61])
			if command[6:9] == "aes":
				self.cryptor = AES()
				self.cryptor.mode = 'dual'
				self.cryptor.setKeys(command[10:42])
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
	
	#basic run of the program
	def run(self):
		#The user enter the server ip address.
		global root
		root = Tk()
		lab = Label(root, text="What server do you want to connect?")
		lab.pack(side=TOP)
		global ent
		ent = Entry(root)
		ent.pack(fill=X)
		ent.focus()
		ent.bind('<Return>', self.fetch)
		btn = Button(root, text="OK", command = self.fetch)
		btn.pack(side=BOTTOM)
		root.mainloop()
		
		self.cryptor = None #in charge of encrypting and decrypting
		
		serverPort = 24766
		global sockobj
		sockobj = socket(AF_INET, SOCK_STREAM)      
		sockobj.connect((self.serverHost, serverPort))
		global gui
		gui = WBGui(server=self)
		gui.printCon('Connected to server: '+self.serverHost+'\n')          
		thread.start_new_thread(self.listen, (sockobj, self.serverHost, ))

		gui.mainloop()
		sockobj.close() 	

if __name__ == "__main__":
		client = WBClient()
		client.run()