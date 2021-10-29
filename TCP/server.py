import socket
from cryptography.fernet import Fernet
from _thread import *


serverSocketTCP =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localIP = socket.gethostbyname(socket.gethostname())
localPort = 8014
buffer = 2048
# Fernet key must be 32 url-safe base64-encoded bytes.
key = b'lt99kum1f2cuaYI8qGQ0HKOJW3weImO49S8661Elq-U=' 
f = Fernet(key)
threadCount = 0

def messageParser(mymessage, connectionSocket):

    print('Il client invia:' + str(mymessage))

    # decodificare la stringa mymessage

    try:
        mymessage = f.decrypt(mymessage).decode('utf-8')
        print('Il client invia:' + mymessage)

        cmd = mymessage.split("|")

        if len(cmd) != 2:
            print("Error: messaggio non formattato correttamente")
            connectionSocket.sendall(f.encrypt(b"ERROR"))
        else:
            # cmd[0] comandi , cmd[1] parametri
            print(cmd)

            if 'DCQ' == cmd[0]:
                    connectionSocket.sendall(f.encrypt(b"QUIT"))

            if 'DCQ' != cmd[0] or 'DCP' != cmd[0] or 'DCN' != cmd[0]:
                connectionSocket.sendall(f.encrypt(b"ERROR"))  
    except:
        connectionSocket.close()



def thread_client(connectionSocket):
    while True:
        response = connectionSocket.recv(buffer)
        if not response:
            break

        messageParser(response, connectionSocket)
    
    #connectionSocket.close()

   


def serverTCP():
    try:
        serverSocketTCP.bind((localIP, localPort))
    except socket.error as e:
        print(str(e))
    
    serverSocketTCP.listen(1)

    while True:
        global threadCount
        print ("Server TCP attivo e in ascolto su: " + localIP  + " " + str(localPort) )
        connectionSocket, addr = serverSocketTCP.accept()

        start_new_thread(thread_client, ((connectionSocket, )))
        threadCount = threadCount + 1
        print("Si p collegato un nuovo client " + str(threadCount))



def main():
    serverTCP()

if __name__ == "__main__":
    main()