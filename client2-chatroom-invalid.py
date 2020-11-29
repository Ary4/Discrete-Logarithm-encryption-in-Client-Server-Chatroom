import socket
import select
import errno
import hashlib
import random
HEADER_LENGTH = 10
g=5
p=1237

IP = "127.0.0.1"
PORT = 8001
my_username = input("Username: ")
# x=(hash(my_username) % 10**8)
x=43

r=random.randint(1,1000)
C=pow(g,r,p)
#if request =0 then give r..
# Create a socket
#else request=1 then give val=(x+r)%p-1
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
# client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)
y=pow(g,x,p)
print(y)
st=str(y)
byt=st.encode()
client_socket.send(byt)
for itr in range(1,6):
    r=random.randint(1,1000)
    C=pow(g,r,p)
    st=str(C)
    byt=st.encode()
    client_socket.send(byt)

    req=client_socket.recv(1024)
    req=req.decode()
    print("req",req)
    req=int(req)
    if(req==0):
        #send r
        st=str(r)
        byt=st.encode()
        client_socket.send(byt)
    else:
        val=pow(r+x,1,p-1)
        st=str(val)
        byt=st.encode()
        client_socket.send(byt)
st=client_socket.recv(1024)
st=st.decode()
print (str(st))
st=client_socket.recv(1024)
st=st.decode()
inv=int(st)
if(inv==1):
    client_socket.close()
else:
    while True:
        client_socket.setblocking(False)
        # Wait for user to input a message
        message = input(f'{my_username} > ')


        # If message is not empty - send it
        if message:

            # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)

        try:
            # Now we want to loop over received messages (there might be more than one) and print them
            while True:

                # Receive our "header" containing username length, it's size is defined and constant
                username_header = client_socket.recv(HEADER_LENGTH)

                # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()

                # Convert header to int value
                username_length = int(username_header.decode('utf-8').strip())

                # Receive and decode username
                username = client_socket.recv(username_length).decode('utf-8')

                # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')

                # Print message
                print(f'{username} > {message}')

        except IOError as e:
            # This is normal on non blocking connections - when there are no incoming data error is going to be raised
            # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
            # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
            # If we got different error code - something happened
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            # We just did not receive anything
            continue

        except Exception as e:
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))
            sys.exit()