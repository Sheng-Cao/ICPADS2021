
a=0
start_time=0.0
bidding=[]
bidder=[]
while a<80:
#while True:
    print("starts, listening for links")
    conn, addr = tcpS.accept()
    print("The linked c", addr)
    bidder.append(addr)
    #while a<100:
    while True:
        try:
            data = conn.recv(BUFSIZ) # Read sent messages from linked customers
            if a==0:
                start_time=time.time()
            bidding.append(data)
            bidder.append(data.decode(COD))
            a=a+1
        except Exception:
            print("Disconnected client", addr)
            break
        
        #print("The content sent by the c",data.decode(COD))
        if not data:
            break
        # msg = input('>>').strip()
        # if msg=='':
        #     msg="get"
        msg="get"
        #msg1 = '[%s]:%s' % (msg, data.decode(COD))
        conn.send(msg.encode(COD)) 
        conn.close() 
        break
    
bidding.sort()
end_time=time.time()
print("aaaaaa")
print((end_time-start_time))
print("ksdhldjs")
print(bidding[0])
tcpS.close()
