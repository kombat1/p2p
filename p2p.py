import socket
import argparse
import sys
import threading

args = argparse.ArgumentParser()
args.add_argument('-p','--port', type=int, help='port',metavar='')
args = args.parse_args()

def server(port):
	sock = socket.socket()
	sock.bind((socket.gethostbyname(socket.gethostname()), port))
	print("Server started your ip",socket.gethostbyname(socket.gethostname()),"\n")
	sock.listen(3)
	conn, addr = sock.accept()
	print("Connected",addr)
	
	while True:
		data = conn.recv(1024)
		if data.decode() == "exit":
			conn.send('end'.encode())
			conn.close()
			break
		if not data:
			conn.send("\n".encode())
		print("Server",data.decode())
		

def client():
	while 1:	
		console = input('~ ')
		array = console.split()
		sock = socket.socket()
		if array[0] == 'connect':
			try:
				input_port = int(array[2])
				sock.connect((array[1], input_port))
				break
			except:
				print("Your don't write port")
				return client()
		elif array[0] == 'exit':
			return SystemExit
		elif array[0] == '':
			return client()	
		else:
			print('Error command')
			return client()
	try:	
		while 1:
			stdin = ''
			while not stdin:
				sock.send(input('>').encode())
			if sock.recv(1024).decode() == "end":
				conn.close()
				break
				return SystemExit
	except:
		pass			


p1 = threading.Thread(target=server, name="t1", args=[args.port])	
p2 = threading.Thread(target=client, name="t2")


p1.start()
p2.start()
