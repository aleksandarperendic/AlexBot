import socket
import argparse
import threading

from Essentials.configFiles import *

# Takes in an argument in terminal. Possible to write "-h" to get some more information about it
arg = argparse.ArgumentParser()
arg.add_argument('port', type=int, help='Write port you are connecting to as server')
allArg = arg.parse_args()
port_server = allArg.port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", port_server))
server_socket.listen()

clients = []
nicknames = []
myBots = ["robot", "coolbot", "babybot", "siribot"]

# Welcome screen - logo / function from configFiles.py
welcome()


# Broadcasting message
def messageToAll(message):
    for client in clients:
        client.send(message)


# Adding command feature on server
def cmd():
    while True:
        cmd = input('Write command: ')
        if cmd == "help":
            help()  # Calls function from configFiles.py
        elif cmd == "time":
            timenow()  # Calls function from configFiles.py
        elif cmd == "cnc":
            connectedClients = len(clients)
            if connectedClients == 0:
                print("No clients connected. Connect the first one.")
            elif connectedClients == 1:
                print("1 client is connected. Connect some more.")
            else:
                print("Connected clients: " + str(connectedClients))
        elif cmd == "whoami":
            print(" ")
            print(bcolors.HEADER + "*****" + bcolors.ENDC)
            print("Hostname: " + socket.gethostname())
            print("You are connected to: " + socket.gethostbyname(socket.gethostname()) + ":" + str(port_server))
            print(bcolors.HEADER + "*****" + bcolors.ENDC)
            print(" ")


cmdT = threading.Thread(target=cmd)
cmdT.start()


def handle(client):
    while True:
        try:
            # Broadcasting message that came
            message = client.recv(1024)
            messageToAll(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            messageToAll('{} does not want to chat with you anymore!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


# Function that listen to connections and inform clients about new connections
def receive():
    while True:
        # Accept connection
        client, address = server_socket.accept()
        # Name checker
        client.send('myname'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        # Sends message to server about new user
        print(" ")
        print("{} is connected with {}".format(nickname, str(address)))
        nicknames.append(nickname)
        clients.append(client)
        # Inform other cliens about new connection
        messageToAll("{} connected on localhost | {}".format(nickname, str(port_server)).encode('utf-8'))

        # Starts threading
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
