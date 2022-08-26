import socket
import re
import argparse
import threading
from Essentials.Bots import *

# Takes in arguments in terminal. Possible to write "-h" to get some more information about arguments
arg = argparse.ArgumentParser()
arg.add_argument('address', type=str, help='Write IP-address you are connecting to')
arg.add_argument('port', type=int, help='Write port you are connecting to as a client')
arg.add_argument('namebot', type=str, help='Write your firstname or name of our bots(RoBOT, CoolBOT, BabyBOT, SiriBOT)')
allArg = arg.parse_args()

# SOURCE : https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3

address = allArg.address
port = allArg.port
name = allArg.namebot
botname = name.lower()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((address, port))


# Listening to server and getting messages
def receiveMessage():
    while True:
        try:
            # Recieve message from server
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'myname':
                client_socket.send(name.encode('utf-8'))
            else:
                # Users have ":" and bots have "-->" between name and message
                if ":" in message:
                    messageSplit = message.lower().split()
                    # Delete all special signs from input. Example: "Wanna play?" --> "Wanna play" (play? --> play)
                    messageSplit = [''.join(e for e in string if e.isalnum()) for string in messageSplit]
                    # Check if message has parts that matches "positive", "negative" or "greeting"
                    if re.compile('|'.join(positive_verbs), re.IGNORECASE).search(message):
                        # Extract found word and puts it as a correct value
                        value = ''.join(map(str, set(messageSplit).intersection(positive_verbs)))
                    elif re.compile('|'.join(negative_verbs), re.IGNORECASE).search(message):
                        value = ''.join(map(str, set(messageSplit).intersection(negative_verbs)))
                    elif re.compile('|'.join(heihei), re.IGNORECASE).search(message):
                        value = ''.join(map(str, set(messageSplit).intersection(heihei)))
                    else:
                        # If word not found on list, sends only string "that" without any meaning
                        value = " that"

                    # Check if "name" is a name of bot
                    if botname == "robot":
                        robot(value, client_socket)
                    elif botname == "coolbot":
                        coolbot(value, client_socket)
                    elif botname == "babybot":
                        babybot(value, client_socket)
                    elif botname == "siribot":
                        siribot(value, client_socket)

                    if botname not in myBots:
                        print(message)
                else:
                    if botname not in myBots:
                        print(message)
        except:
            client_socket.close()
            break


# Sending all messages to server
def writeMessage():
    while True:
        message = input('')
        messageSend = name + ": " + message
        client_socket.send(messageSend.encode('utf-8'))


# Starting receive thread for all clients
receive_thread = threading.Thread(target=receiveMessage)
receive_thread.start()

# Starting write thread for all clients but not bots
if botname not in myBots:
    write_thread = threading.Thread(target=writeMessage)
    write_thread.start()
