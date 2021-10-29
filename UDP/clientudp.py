from socket import *

def clientUDP():
    serverName = '127.0.0.1'
    serverPort = 9000

    clientSocketUDP = socket(AF_INET, SOCK_DGRAM)

    
    for number in range(1000):
        message = "Client UDP" + str(number)
        clientSocketUDP.sendto(message.encode(), (serverName, serverPort))

        #bytesRead = clientSocketUDP.recvfrom(1024)
        #print(str(bytesRead)) 

    clientSocketUDP.close()

def main():
    clientUDP()

if __name__ == "__main__":
    main()