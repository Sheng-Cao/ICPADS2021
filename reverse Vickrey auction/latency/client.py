HOST = gethostname()  # 服务端ip
PORT = 21566  # 服务端端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
a=0
while a<80:
#while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM) 
    tcpCliSock.connect(ADDR)  # connect to server
    #data = input('>>').strip()
    data=str(random.random())
    if not data:
        tcpCliSock.close() 
        continue
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ) 
    if not data:
        continue
    print(data.decode('utf-8'))
    tcpCliSock.close() 
