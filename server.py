import socket
# import time
import threading
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip = socket.gethostbyname(socket.gethostname()) #suitable to host to the outside network
ip = "localhost"
port = 5050

sock.bind((ip, port))
sock.listen()
print('started listening at', ip)
online_people = {}

def findpersonbyname(name):
	global online_people
	for i in online_people:
		if i.lower() == name.lower():
			return online_people[i]

def send_to_all(message):
	global online_people
	temp = []
	for person in online_people:
		try:
			online_people[person].send(bytes(message, 'utf-8'))
		except BrokenPipeError:
			print('unable to send message to', person)
			temp.append(person)
	
	for disconnected in temp:
		try:
			del online_people[disconnected]
		except KeyError:
			pass

def listen_to_client(client, addr):
	global online_people
	username = 'No Name'
	# online_people[client] = None
	while True:
		try:
			msg = client.recv(2048)
			msg = msg.decode('utf-8')
		except ConnectionResetError:
			send_to_all('β'+str(username)+ ' has left the chat!')
			try:
				del online_people[username]
			except KeyError:
				pass
			break
		if not msg:
			send_to_all('β'+str(username)+ ' has dissapeared')
			try:
				del online_people[username]
			except KeyError:
				pass
			break
		elif msg == 'exit':
			send_to_all('β'+username+' has left the chat')
			try:
				del online_people[username]
			except KeyError:
				pass
			client.close()
			break
		elif msg.startswith('α'):
			username = msg[1::]
			online_people[username] = client
			send_to_all('γ'+username+' has joined the chat')

		elif msg.startswith('/w'):
			name = msg.split()[1]
			c = findpersonbyname(name)
			if c:
				try:
					c.send(bytes('∑'+username+'|'+msg.split()[2], 'utf-8'))
					client.send(bytes('\033[90mYou Whispered to '+name+'\033[0m', 'utf-8'))
				except IndexError:
					client.send(b'[SERVER]Invalid Syntax/Request!')
			else:
				client.send(b'[SERVER]Could Not Find a Person Online With that Name')
		elif msg:
			# print(addr[0], 'has sent:', msg)
			send_to_all('ø'+username+'|'+msg)

while True:
	connection, address = sock.accept()
	x = threading.Thread(target=listen_to_client, args=(connection, address))
	x.start()
	print(address[0], 'has connected!')