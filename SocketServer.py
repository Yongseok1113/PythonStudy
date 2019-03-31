import socket

#서버 소켓 준비
server = socket.socket()
server.bind( ('192.168.219.104', 9999) )

#들어올때까지 기다림
server.listen(1)

print('Server is ready')

#클라이언트 접속 수락
client, addr = server.accept()
print('client is connected')

#메시지 수신
msg = client.recv(1024)
print('Message received')
print(msg)

#메시지 송신
client.sendall( b'Hi i\'m server. your message is \''+ msg + b'\'' )

#CS 해제
client.close()
server.close()
