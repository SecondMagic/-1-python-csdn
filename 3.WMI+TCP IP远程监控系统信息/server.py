#coding:utf-8
import socket
import threading
import time
import sys                                                                    
import signal
def saveInfo(info):
#	try:
		fileAll='d:\\1\\tcp\\data.txt'
		with open(fileAll,'a',encoding='utf-8') as file_write:
			file_write.write(info+'\n')
#	except:
#		print('error:something faile')
#def quit(signum, frame):  
#    print('') 
#    print('stop fusion')  
#    sys.exit()
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    buffer = []#
    while True:
        data = sock.recv(1024)
        if data:
            buffer.append(data)
        else :
            break
        #sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    dataStr = b''.join(buffer)
    if mutex.acquire(True):
        saveInfo(str(dataStr,'utf-8'))
        print(dataStr)
        mutex.release()
	
#signal.signal(signal.SIGINT, quit)                                  
#signal.signal(signal.SIGTERM, quit)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('服务器地址', 9999))
s.listen(5)
threads = []
mutex = threading.Lock()
print('Waiting for connection...')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr)) 
    threads.append(t)
    t.start()
	