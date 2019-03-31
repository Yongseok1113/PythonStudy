import socket
import sys

ip = '192.168.219.104'
port = 9999

client = socket.socket()
client.connect((ip,port))

file = open("C:/Users/ysoh/Desktop/sampleImg.jpg", "rb")

l = file.read(1024)
while (l) :
    client.send(l)
    l = file.read(1024)

client.close()