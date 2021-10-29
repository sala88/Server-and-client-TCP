import socket
from cryptography.fernet import Fernet
#import psutil             

clientSocketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 8014
buffer = 2048
# Fernet key must be 32 url-safe base64-encoded bytes.
key = b'lt99kum1f2cuaYI8qGQ0HKOJW3weImO49S8661Elq-U=' 
f = Fernet(key)

def clientTCP():
    print(host + " " + str(port))
    try:
        clientSocketTCP.connect((host, port))
    except socket.error as e:
        print(str(e))

    while True:
        message = input() # Temperatura cpu
        #message = str(psutil.cpu_percent(interval=1))
        clientSocketTCP.send(f.encrypt(message.encode()))
        mymessage = clientSocketTCP.recv(buffer) # Receive

        response = f.decrypt(mymessage).decode('utf-8')
        print(response)
        if "QUIT" in response:
            print("il serve chiude la socket")
            clientSocketTCP.close()
            exit()

def main():
    clientTCP()

if __name__ == "__main__":
    main()