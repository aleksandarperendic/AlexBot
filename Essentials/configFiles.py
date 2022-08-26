from datetime import datetime


#    ___                       __     _      __ _
#   / __|    ___    _ _       / _|   (_)    / _` |
#  | (__    / _ \  | ' \     |  _|   | |    \__, |
#   \___|   \___/  |_||_|   _|_|_   _|_|_   |___/
# _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|
# "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
# Configuration file contains coloring, welcome-screen and some server-commands


# Inspiration for colouring: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Welcome screen
def welcome():
    print(" ")
    print(bcolors.FAIL + "          _           ____        _   " + bcolors.ENDC)
    print(bcolors.FAIL + "    /\   | |         |  _ \      | |  " + bcolors.ENDC)
    print(bcolors.FAIL + "   /  \  | | _____  _| |_) | ___ | |_ " + bcolors.ENDC)
    print(bcolors.FAIL + "  / /\ \ | |/ _ \ \/ /  _ < / _ \| __|" + bcolors.ENDC)
    print(bcolors.FAIL + " / ____ \| |  __/>  <| |_) | (_) | |_ " + bcolors.ENDC)
    print(bcolors.FAIL + "/_/    \_\_|\___/_/\_\____/ \___/ \__|" + bcolors.ENDC)
    print(" ")
    print(bcolors.HEADER + "Connected to AlexBot server" + bcolors.ENDC)
    print(" ")
    print("Test some commands: 'help', 'time', 'cnc', 'whoami'")
    print(" ")


# Function for help command on server
def help():
    print("If you need help to connect as a client, write 'client', if you want to connect some of bots, write 'bot'")
    message = input(">>")
    if message == "client":
        print(" ")
        print(bcolors.BOLD + "*****" + bcolors.ENDC)
        print(
            "To start chat as a client write: " + bcolors.FAIL + "python3 TCP_Client.py localhost PORT_NUMBER YOUR_NAME" + bcolors.ENDC)
        print(bcolors.BOLD + "*****" + bcolors.ENDC)
        print(" ")
    elif message == "bot":
        print(" ")
        print(bcolors.BOLD + "*****" + bcolors.ENDC)
        print(
            "To start chat as a bot write: " + bcolors.FAIL + "python3 TCP_Client.py localhost PORT_NUMBER BOT_NAME" + bcolors.ENDC)
        print("Available bots: ")
        print(bcolors.HEADER + "                RoBOT" + bcolors.ENDC)
        print(bcolors.HEADER + "                CoolBOT" + bcolors.ENDC)
        print(bcolors.HEADER + "                BabyBOT" + bcolors.ENDC)
        print(bcolors.HEADER + "                SiriBOT" + bcolors.ENDC)
        print(
            "Botname is not case-sensitive. You can write " + bcolors.HEADER + "robot" + bcolors.ENDC + " or " + bcolors.HEADER + "RoBOT" + bcolors.ENDC + " and you will connect to RoBOT")
        print(bcolors.BOLD + "*****" + bcolors.ENDC)
        print(" ")


# Function that prints current date/time on server
def timenow():
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M")
    print(" ")
    print(bcolors.HEADER + "*****" + bcolors.ENDC)
    print("Current date: " + current_date)
    print("Current time: " + current_time)
    print(bcolors.HEADER + "*****" + bcolors.ENDC)
    print(" ")
