# Discrete-Logarithm-encryption-in-Client-Server-Chatroom

Discrete logarithm problem can exploited in encryption to obtain hard to break but open messages code.In this project,we additionally provide another layer of encryption in Client-Server Socket. It has been further modified to incorporate a chat-room. Python 3 is used,so each and every message is encoded and sent where as the receiver has to decode that message to access it(unlike python2 where you can freely send message through sockets).  

DiscreteLog.cpp is an example of how our algorithm works.So,if its your first time understanding ZKP,it will be a good example of how the algorithm.Refer to slides as well for the protocol.
client1.py and server1.py is a pair program for server client 2way interaction(no other user can join in) .You can uncomment the code to incorporate it to store data in csv files which i wont recommend.
client2-chatroom.py and server2-chatroom.py is an extension of above program with simple hosting a chatroom.
If you are using windows,you might need to allow firewall access to python to host a port.(Remote host not found kind of error)
If you have any question,ping me.

