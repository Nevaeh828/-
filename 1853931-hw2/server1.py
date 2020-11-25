# 使用python中的网络编程
import socket
import time
import subprocess

# 创建一个tcp/ip协议的套接字
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建一个udp/ip的套接字
# udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "localhost"
port = 8888
buffer_size = 1024
address = (host, port)
# 开始绑定地址
tcpSocket.bind(address)
tcpSocket.listen(5)

while True:
    print("服务器等待被连接中···")
    clientSock, client_addr = tcpSocket.accept()
    print("已经连接到客户端，连接地址：{0}".format(client_addr))
    try:
        while True:        		
            data = clientSock.recv(buffer_size)
            author=str(data, encoding="utf8")
            if author == "Socket2 wrong":
            	newdata=author.replace(' ','[[:space:]]')
            	output = subprocess.check_output('grep -o %s dblp_1.xml | wc -l' % newdata, shell=True)
            	clientSock.send(output)
         
            newdata=author.replace(' ','[[:space:]]')
  
            output = subprocess.check_output('grep -o %s dblp_0.xml | wc -l' % newdata, shell=True)
            clientSock.send(output)
            print(output)
            print("接收客户端的数据为：{0}".format(str(data, encoding="utf8")))
            if data.upper() == "EXIT":
                break
            
		
    except Exception as e:
        print(e)
        clientSock.send("wrong")
        # 异常处理 把消息返回给客户端
        
    finally:
        clientSock.close()

tcpSocket.close()


