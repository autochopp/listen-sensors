import socket

TCP_IP = '192.168.0.15'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print "Up and running!!"
    conn, addr = s.accept()
    print 'Connection address:', addr

    while 1:
        try:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            print "received data:", data
            conn.send("Resent:%s"%data)  # echo
        except KeyboardInterrupt:
            conn.close()
            print "Server closed"
            break
except KeyboardInterrupt:
    print "Server closed"

