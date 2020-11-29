# Import socket module 
import socket     
import getpass
import hashlib    
import random       
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 8081
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
 
g=23
p=1237
# receive data from the server
 
st=s.recv(1024)
st.decode()
print (str(st))

uid = input("\nEnter Userid : ")
pw = input('Password: ')
x=int(pw)
#pw=input("Enter Password : ")
st=str(uid)
byt=st.encode()
s.send(byt)
y=pow(g,x,p)
st=str(y)
byt=st.encode()
s.send(byt)
for itr in range(1,6):
    r=random.randint(1,10)
    C=pow(g,r,p)
    st=str(C)
    byt=st.encode()
    s.send(byt)

    req=s.recv(1024)
    req=req.decode()
    print("req",req)
    req=int(req)
    if(req==0):
        #send r
        st=str(r)
        byt=st.encode()
        s.send(byt)
    else:
        val=pow(r+x,1,p-1)
        st=str(val)
        byt=st.encode()
        s.send(byt)
st=s.recv(1024)
st=st.decode()
print (str(st))
s.close()



    
    # pw1=pw.encode()
#     hash_object = hashlib.sha1(pw1)
#     hex_dig = hash_object.hexdigest()
#     hsh=int(hex_dig,16)
#     x=hsh%100
#     #print (x)
#     y=(2**x) # g0 =5
#     T1=(2**r) #r :random number

#     inpu=str(y+T1+a)
#     inpu1=inpu.encode()
#     hash_object = hashlib.sha1(inpu1)
#     hex_dig = hash_object.hexdigest()
#     hsh=int(hex_dig,16)
#     c=hsh%100
#     z=r-(c*x)
#     #print z
#     #print c
#     #print z
#     #print T1
#     st=str(z)
#     byt=st.encode()
#     s.send(byt)
#     st=str(c)
#     byt=st.encode()
#     s.send(byt)
#     st=s.recv(1024)
#     byt=st.decode()
#     print (str(byt))

# else :
#     st=s.recv(1024)
#     st.decode()
#     print (str(st)) #signup
#     uid = input("\nEnter Userid : ")
#     pw = getpass.getpass('Password: ')
#     #pw=input("Enter Password : ")
#     st=str(uid)
#     byt=st.encode()
#     s.send(byt)
    
#     pw1=pw.encode()
#     print(pw1)
#     hash_object = hashlib.sha1(pw1)
#     hex_dig = hash_object.hexdigest()
#     hsh=int(hex_dig,16)
#     x=hsh%10
#     #print x 
#     y=(2**x) # g0 =5
#     #print y 
#     st=str(y)
#     byt=st.encode()
#     s.send(byt)
#     # s.send(str(y))


# # print (s.recv(1024))
# st=s.recv(1024)
# st=st.decode()
# print (str(st)) 
# # close the connection 
# s.close()        