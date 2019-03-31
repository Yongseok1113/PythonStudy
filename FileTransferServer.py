import socket
import sys

ip = '192.168.219.104'
port = 9999

server = socket.socket()

server.bind((ip,port))
server.listen(5)

print('Server is ready')

#파일번호
i = 1

while True:
    #클라이언트 접속수락
    client, address = server.accept()
    print('client is connected')
    print('adress : {0}'.format(address))

    #파일 열기(binary)
    file = open('C:/Users/ysoh/Desktop/'+ str(i) + '.jpg', 'wb')
    i = i + 1
    print('i : {0}'.format(i))

    l = 1
    while(1) :
        l = client.recv(1024)
        print('data --> {0}'.format(l))
        while(l) :
            file.write(l)
            l = client.recv(1024)
        file.close()

    client.close()

server.close()




