import socket


#서버 ip & port
ip = '192.168.219.104'
port = 9999

#클라이언트 소켓준비
client = socket.socket()

#서버접속
client.connect((ip, port))

print('Server is connected')

#메세지 송신

client.send(b'Hello i\'m client!')

print('Message send success')

#메세지 수신

msg = client.recv(1024)

print('Message receive success : ', msg)

client.close


