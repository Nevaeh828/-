# 使用python中的网络编程
import socket
import time
import logging

# 创建一个tcp/ip协议的套接字
clientSocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建一个udp/ip的套接字
# udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "localhost"
port1 = 8888
port2 = 9999
buffer_size = 1024
address1 = (host, port1)
address2 = (host, port2)
# 开始连接服务器地址
clientSocket1.connect(address1)
clientSocket2.connect(address2)
if clientSocket1 is None:
    print("无法连接当前的服务器！")
else:
    print("已经连接服务器---> ok")
    while True:
        data = input("发送数据到服务器：(exit/quit退出)")
        start = time.perf_counter()
        if data.lower() == "exit" or data.lower() == "quit":
            clientSocket1.send(bytes("EXIT", encoding="utf8"))
            clientSocket2.send(bytes("EXIT", encoding="utf8"))
            # 关闭当前的客户端
            clientSocket1.close()
            clientSocket2.close()
            break

        clientSocket1.send(bytes(data, encoding="utf8"))
        clientSocket2.send(bytes(data, encoding="utf8"))
        
        # 接收并处理服务器发送的数据
        data1 = clientSocket1.recv(buffer_size)
        if data1 == "wrong":
        	clientSocket2.send(bytes("Socket1 wrong", encoding="utf8"))
        	data1 = clientSocket2.recv(buffer_size)
        data1 = str(data1,encoding="utf-8")
        data1 = data1.strip('\n')
        
        data2 = clientSocket2.recv(buffer_size)
        if data2 == "wrong":
        	clientSocket1.send(bytes("Socket2 wrong", encoding="utf8"))
        	data2 = clientSocket1.recv(buffer_size)       
        data2 = str(data2,encoding="utf-8")
        data2 = data2.strip('\n')
        
        
        n1 = int(data1)
        n2 = int(data2)
        # 打印接收的数据
        f = open("1853931-hw2-q1.log", "w+")
        print('socket1:{0}'.format(n1), file = f)
        print('socket2:{0}'.format(n2), file = f)
        n=n1+n2
        print('{0}:{1}'.format(data, n), file = f)
        print(n1)
        print(n2)
        print(n)
        # print('socket1:{0}'.format(n1))
        # print('socket2:{0}'.format(n2))
        print(tottime)
        end = time.perf_counter()
        tottime=end-start
        print('Running time: {0} Seconds'.format(tottime), file = f)


