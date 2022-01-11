import socket
import threading
import os
def encrypted(a):
	b = list(reversed(a))
	c = []
	s = ''
	for i in range(len(b)):
		c = c + [chr(ord(b[i])+120)]
	for i in c:
		s = s + i
	return s

def decrypted(a):
	b = list(a)
	c = []
	s = ''
	for i in range(len(b)):
		c = c + [chr(ord(b[i]) - 120)]
	for i in list(reversed(c)):
		s = s + i
	return s

os.system('clear')
messages_to_display = []
print('''


			┏━━━┓╋╋╋┏┓┏┓╋╋╋╋╋╋╋╋┏━━━┳┓╋╋╋╋┏┓
			┃┏━┓┃╋╋┏┛┗┫┃╋╋╋╋╋╋╋╋┃┏━┓┃┃╋╋╋┏┛┗┓
			┃┗━┛┣┓╋┣┓┏┫┗━┳━━┳━┓╋┃┃╋┗┫┗━┳━┻┓┏┛
			┃┏━━┫┃╋┃┃┃┃┏┓┃┏┓┃┏┓┓┃┃╋┏┫┏┓┃┏┓┃┃
			┃┃╋╋┃┗━┛┃┗┫┃┃┃┗┛┃┃┃┃┃┗━┛┃┃┃┃┏┓┃┗┓
			┗┛╋╋┗━┓┏┻━┻┛┗┻━━┻┛┗┛┗━━━┻┛┗┻┛┗┻━┛
			╋╋╋╋┏━┛┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋
			╋╋╋╋┗━━┛╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋



''')
while True:
	username = input('\t\t\t\tEnter your Name:')
	if ' ' in username:
		print('\t\t\t\t\033[91mInvalid Username, You are not allowed to use Space(" ")\033[0m')
	else:
		break

def display(messages_list):
	os.system('clear')
	print('\n'*40)
	print('\a', end=None)
	for msg in messages_list:
		if msg.startswith('ø'):
			author = msg.split('|')[0]
			message = msg.split('|')[1]
			print('\033[93m'+author[1::]+':\033[0m')
			print(decrypted(message), '\n')
		elif msg.startswith('∑'):
			author = msg.split('|')[0]
			message = msg.split('|')[1]
			print('\033[96m'+author[1::]+':\033[0m')
			print(decrypted(message), '\n')
		else:
			if msg.startswith('β'):
				print('\033[90m'+msg[1::]+'\033[0m', end='\n\n')
			elif msg.startswith('γ'):
				print('\033[92m'+msg[1::]+'\033[0m', end='\n\n')
			else:
				print(msg, end='\n\n')

	print('_________________________________________________________')
	print('Enter Message:', end='', flush=True)

def background_thread():
	global messages_to_display
	while True:
		message = sock.recv(2048)
		y = message.decode('utf-8')
		if y == '':
			print('\033[91m[ERROR]The server has CRASHED!\033[0m')
			break
		else:
			messages_to_display.append(y)
			display(messages_to_display)

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
name = socket.gethostname()
try:
	sock.connect(('localhost' , 5050))
except:
	print('\033[91mSorry, the Server is Currently Offline!\033[0m')
	exit()
print('We have successfully connected to the host')
print('\n\n')


sock.send(bytes('α'+username, 'utf-8'))
print('\n\n')
os.system('clear')

x = threading.Thread(target = background_thread, daemon=True)
x.start()
while True:
	m = input()
	if m == 'exit':
		sock.send(bytes('exit', 'utf-8'))
		break
	elif m.startswith('/w'):
		encrypted_whisper = m.split()[0]+' '+m.split()[1]+' '+encrypted(' '.join(m.split()[2::]))
		sock.send(bytes(encrypted_whisper, 'utf-8'))
	elif m:
		sock.send(bytes(encrypted(m),'utf-8'))

