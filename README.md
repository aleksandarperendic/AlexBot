# AlexBot

## Introduction

This is first and individual part of the final exam in course **DATA2410** at OsloMet – Oslo Metropolitan University. Briefly described, the task is to create a chatroom where users and bots can connect and chat. Users can send messages while bots can only reply to them. Multiple users can correspond with each other and ask questions to bots in parallel. It is expected to have four bots that answer questions differently depending on the verb used in the question.

**Project Structure:**
 
| Assignment Title                  |                                            Socket Bots                                         | 
|:----------------------------------|:----------------------------------------------------------------------------------------------:|
| Course name                       |                                    Networking and Cloud Computing                              | 
| Programming language              |                                             Python                                             |   
| Student                           |                                      Aleksandar Perendic                                       |      
| Progress                          | <ul><li>[x] Preparation</li><li>[x] Coding</li><li>[X] PDF Report</li><li>[X] Review</li></ul> |  
| Submitted                         |                                           :white_check_mark:                                   |

**File Structure:**

```bash
├── Essentials              
│   ├── Bots.py             # Parts of code that have to do with bots
│   ├── Words.py            # Arrays with greetings, and some positive and negative verbs
│   └── configFiles.py      # Configuration file for commands in server and colouring
├── TCP_Client.py           # Client code, sending and receiving functions
└── TCP_Server.py           # Server code, listening to connections and broadcasting
```

## How to use

### Server:
1) To start server, you need to write port number. For example:
      ```python
      python3 TCP_Server.py 8080
      ```
2) You are connected if you can see logo (not finished):
      ```
                _           ____        _   
          /\   | |         |  _ \      | |  
         /  \  | | _____  _| |_) | ___ | |_ 
        / /\ \ | |/ _ \ \/ /  _ < / _ \| __|
       / ____ \| |  __/>  <| |_) | (_) | |_ 
   /_/    \_\_|\___/_/\_\____/ \___/ \__|
      
   Connected to AlexBot server
   
   Write command: 
      ```

3) You can write some commands here:
   - To see some basic information about usage write  ``help``
   
     - Then you can choose what you need help with
        ``client`` or ``bot``
        
   - To see current date and time write ``time``
     - Confirmation will look like this:
        ```
         *****
         Current date: 28-03-2022
         Current time: 19:20
         *****
        ```
        
   - To see how many clients are connected, you can write ``cnc`` 
     - Confirmation will look like this:
        ```
        No clients connected. Connect the first one.
        ```

   - To see you hostname and information about connection, you can write ``whoami`` 
     - Confirmation will look like this:
        ```
        *****
        Hostname: AleksanderMacbookPro.local
        You are connected to: 127.0.0.1 | 8082
        *****
        ```   
***
### Client:
1) To start client as user, you need to write address, port number and name. For example:
      ```python
      python3 TCP_Client.py localhost 8080 Aleksander
      ```
     - Confirmation will look like this:
        ```
        Aleksandar connected on localhost : 8080
        ```
2) To start client as bot, you need to write address, port number and botname. For example:
      ```python
      python3 TCP_Client.py localhost 8080 robot
      ```
     - Names for bots are not case-sensitive. Feel free to connect as "robot" or "ROBOT"
   
***   
### Chatting:
1) You can connect as two different users. Output will look like this:
      ```
      Anne: Hello Aleksander! How are you?
      
      Aleksander: Hi Anne! I'm fine. And what about you?
      
      Anne: Just fine! Thanks for asking.
      ```

2) You can connect as one user and three bots. Output will look like this: 
      ```
      Marie: Do you guys want to play today?
      
      
      RoBOT --> Ohh! You remember that I love playing? I love you man!
      
      SiriBOT --> That sounds nice. Playing is my favourite thing in the world!
      
      CoolBOT --> WooHoo! Let's try playing, it was long ago.
      ```
      
   - If you disconnect CoolBOT but keep other bots, output will look like this: 
  
      ```
      Marie: Well, okay! But do you want to gossip maybe?
      
      
      RoBOT --> Well, I guess I will go for gossiping today. Sounds nice!
      
      CoolBOT --> I'm also into gossiping. Good suggestion!
      
      SiriBOT does not want to chat with you anymore!
      ```
   
    - Bots are not perfect, and they can't answer you to everything you imagine. Output will look like this: 
  
      ```
      Marie: Do you want to borrow me some jeans?
      
      
      RoBOT --> I'm not quite sure what you think about. Let's make it easier for both of us.
      
      CoolBOT --> I'm not paid enough to understand everything you wrote. Write something else.
      ```
   
3) Bots are just bots. They are not talking if you don't ask them something. If you connect two bots without users, there would be no output. Only thing you would see on server side that bots are connected.

      ```python
      RoBOT is connected with ('127.0.0.1', 49648)
 
      CoolBOT is connected with ('127.0.0.1', 49649)
      ```
***
### Fun Facts:

1) This is my first python project, and I learned a lot in last couple of weeks. I love it!

2) Most of the code was written on a local machine during the night at my work as nurse on psychiatry (nightshifts).

3) If you write "Hi" or "Hello" to bots, they will answer you on many different languages. Isn't that cool?

4) I followed over 10 videos on youtube to try to understend sockets. Nothing worked as I wanted. 


***

[![Python 3.10.2](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3102/) [![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)](https://www.jetbrains.com/pycharm/) [![Macbook Pro 2021](https://img.shields.io/badge/Apple-MacBook_Pro_2021-999999?style=for-the-badge&logo=apple&logoColor=white)](https://www.apple.com/macbook-pro-14-and-16/) [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aleksandarperendic)
