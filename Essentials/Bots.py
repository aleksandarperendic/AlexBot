import random
from Essentials.Words import *

#      * * * * * * * * * * * * * * * * * * * * * * * * * *
#      *   List of all bots that can be used in a chat:  *
#      *   Name of bots:                                 *
#      *          1) RoBOT                               *
#      *          2) CoolBOT                             *
#      *          3) BabyBOT                             *
#      *          4) SiriBOT                             *
#      * * * * * * * * * * * * * * * * * * * * * * * * * *


# Inspiration for names: https://www.soocial.com/chatbot-names/
myBots = ["robot", "coolbot", "babybot", "siribot"]


# First bot with the name "RoBOT". Function takes a word from client and client_socket
def robot(word, client):
    if word in heihei:
        # Random choice of greeting on many langauges
        answer = random.choice(greeting)
        message = "\nRoBOT --> " + answer + "!\n"
        client.send(message.encode('utf-8'))

    elif word in positive_verbs:
        answer = [
            "\nRoBOT --> OMG!!! How could I forget about {}? That would be awesome!\n".format(word + "ing"),
            "\nRoBOT --> Well, I guess I will go for {} today. Sounds nice!\n".format(word + "ing"),
            "\nRoBOT --> Ohh! You remember that I love {}? I love you man!\n".format(word + "ing")
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))

    elif word in negative_verbs:
        answer = [
            "\nRoBOT --> Njaaa. I'm not quiet sure about {}. Why don't we try something else?\n".format(word + "ing"),
            "\nRoBOT --> I don't like how you think. You know that {} is a bit boring, right?\n".format(word + "ing"),
            "\nRoBOT --> I would rather not, {} seems creepy.\n".format(word + "ing")
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))

    else:
        answer = [
            "\nRoBOT --> I'm not quite sure what you think about. Let's make it easier for both of us.\n",
            "\nRoBOT --> Hmm... Can you write something else? I'm still a bit stupid.\n",
            "\nRoBOT --> I'm a bit shy and I can't answer you to that.\n"
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))


# Second bot with the name "CoolBOT"
def coolbot(word, client):
    if word in heihei:
        answer = random.choice(greeting)
        message = "\nCoolBOT --> " + answer + "!\n"
        client.send(message.encode('utf-8'))

    elif word in positive_verbs:
        answer = [
            "\nCoolBOT --> God bless you, {} is something I was just thinking to suggest.\n".format(word + "ing"),
            "\nCoolBOT --> WooHoo! Let's try {}, it was long ago.\n".format(word + "ing"),
            "\nCoolBOT --> I'm also into {}. Good suggestion!\n".format(word + "ing")
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))

    elif word in negative_verbs:
        answer = [
            "\nCoolBOT --> What's wrong with you? The last thing I would do right now is {}.\n".format(word + "ing"),
            "\nCoolBOT --> C'mon my friend! Nobody is into {} in 2022.\n".format(word + "ing"),
            "\nCoolBOT --> No. If I can choose between drinking a coffee or {}, you know what I choose.\n".format(
                word + "ing")
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))

    else:
        answer = [
            "\nCoolBOT --> Can you try to write something easier? My boss is about to fire me!\n",
            "\nCoolBOT --> I'm not paid enough to understand everything you wrote. Write something else.\n",
            "\nCoolBOT --> Wait a moment! What do you mean by" + "{}".format(word) + "? Is that something we can eat?\n"
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))


# Third bot with the name "BabyBOT"
def babybot(word, client):
    if word in heihei:
        answer = random.choice(greeting)
        message = "\nBabyBOT --> " + answer + "!\n"
        client.send(message.encode('utf-8'))

    elif word in positive_verbs:
        answer = [
            "\nBabyBOT --> OMG, {} is so, so, so cool. Let's do it!\n".format(word + "ing"),
            "\nBabyBOT --> I'm totally into {}. Wanna start now?\n".format(word + "ing"),
            "\nBabyBOT --> Sure! Let's start {}. Maybe some other suggestions to?\n".format(word + "ing")
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))

    elif word in negative_verbs:
        answer = [
            "\nBabyBOT --> How about no? I'm not into {}...\n".format(word + "ing"),
            "\nBabyBOT --> I give up! Who would do {} today? Nobody.\n".format(word + "ing"),
            "\nBabyBOT --> Ehh.. If I can choose between sleeping or {}, you know what I choose.\n".format(word + "ing")
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))

    else:
        answer = [
            "\nBabyBOT --> Can you try to write some other verbs?\n",
            "\nBabyBOT --> Your message is sent to my lawyer.\n",
            "\nBabyBOT --> Brothers and sisters, I'm still stupid little baby. Write something else\n"
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))


# Third bot with the name "BabyBOT"
def siribot(word, client):
    if word in heihei:
        answer = random.choice(greeting)
        message = "\nSiriBOT --> " + answer + "!\n"
        client.send(message.encode('utf-8'))

    elif word in positive_verbs:
        answer = [
            "\nSiriBOT --> That sounds nice. {} is my favourite thing in the world!\n".format(word + "ing"),
            "\nSiriBOT --> I really like {} as well. I'm gonna do it right away.\n".format(word + "ing"),
            "\nSiriBOT --> I love {}. You wanna do it tonight?\n".format(word + "ing")
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))

    elif word in negative_verbs:
        answer = [
            "\nSiriBOT --> I'm really not a fan of {}. Rather not?\n".format(word + "ing"),
            "\nSiriBOT --> {} is not my favourite thing in the world.\n".format(word + "ing"),
            "\nSiriBOT --> I'm just a bot. This {} is not in my approved dictionary. So, no thanks!\n".format(word + "ing")
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))

    else:
        answer = [
            "\nSiriBOT --> I'm still learning about human interaction. Please write something else.\n",
            "\nSiriBOT --> My computational alghoritm is still a work in progress.\n",
            "\nSiriBOT --> Habibi, you really think I'm so smart? Not really.\n"
        ]
        message = random.choice(answer)
        client.send(message.encode('utf-8'))
