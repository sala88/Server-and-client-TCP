from socket import *

def serverUDP():
    localIP = '127.0.0.1'
    localPort = 9000

    serverSocketUDP = socket(AF_INET, SOCK_DGRAM)

    serverSocketUDP.bind((localIP, localPort))

    print ("server UDP attivo e in ascolto")

    while(True):
        bytesRead = serverSocketUDP.recv()
        
        print(str(bytesRead)) 
        serverSocketUDP.sendto(b"Sono il server UDP, ho ricevuto: " + bytesRead[0], bytesRead[1])

def main():
    serverUDP()

if __name__ == "__main__":
    main()