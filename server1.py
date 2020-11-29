# first of all import the socket library 
import socket    
import csv   
import random  
import hashlib       

# next create a socket object 
s = socket.socket()          
print ("Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 8081

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port))

# put the socket into listening mode 
s.listen(5)      
print ("socket is listening" )           

# a forever loop until we interrupt it or  
# an error occurs 
req= 2
#with open('Users.csv','w') as newFile:
#	newFileWriter = csv.writer(newFile)
#	newFileWriter.writerow(['user_id','Password'])

g=23
p=1237

while True: 

	# Establish connection with client. 
	c, addr = s.accept()      
	print ('Got connection from', addr )
	st='Login Procedure initiating'
	byt=st.encode()
	c.send(byt)
	

	# a=random.randint(1,10)
	# st=str(a)
	# byt=st.encode()
	# c.send(byt) #random number a is generated
	uid=c.recv(1024)
	uid=uid.decode()

	y=c.recv(1024) #y is the encrypted pass of x
	y=y.decode()
	y=int(y)
	inv=0
	#lets say five times for verifying the identity
	for itr in range(1,6):
		print("Iteration: ", itr)

	#Client creates a random value r and sends computated value C and sends it to y
		C=c.recv(1024)
		C=C.decode()
		C=int(C)
	#Server sends a req 0 or 1 to the client
	#if zero check if C==g^rmod p,i.e he asks for the value r and checks in its local generator whether it matches
	#if one check C.y mod p== g^(r+x mod p-1) mod p
		req=random.randint(0,1)
		st=str(req)
		byt=st.encode()
		c.send(byt)
		val=c.recv(1024)
		val=val.decode()
		val=int(val)
		if(req==0):
			chk= pow(g,val,p)
			if(chk==C):
				print("Correct,moving to next iteration\n")
			else:
				# print("Incorrect,Invalid user\n")
				inv=1
				#end connection
				break
				#end the rest of loop
		else:
			
			chk=pow(g,val,p)
			newC=pow(C*y,1,p)
			if(chk==newC):
				print("Correct,moving to next iteration\n")
			else:
				print("Incorrect,Invalid user\n")
				inv=1
				#end connection
				break
	if(inv==0):
		# print("Connection successfully Granted\n")
		st='Connection granted'
		byt=st.encode()
		c.send(byt)
		c.close()
	else:
		print("Connection terminated\n")
		st='Illegitmate access'
		byt=st.encode()
		c.send(byt)
		c.close()


				








	# st="\n 1->Login \n 2->NewUser"
	# byt=st.encode()
	# c.send(byt)
	# req=c.recv(1024)
	# req.decode()
	# req=int(req)

	# rows=[]

	# if req==1:
	# 	st='Login Procedure initiating'
	# 	byt=st.encode()
	# 	c.send(byt)
	# 	a=random.randint(1,10)
	# 	st=str(a)
	# 	byt=st.encode()
	# 	c.send(byt) #random number a is generated
	# 	uid=c.recv(1024)
	# 	uid=uid.decode()
	# 	#print(str(a)+'\n')
	# 	#print(str(uid))

	# 	z=c.recv(1024)
	# 	z=z.decode()
	# 	c1=c.recv(1024)
	# 	c1=c1.decode()
	# 	c1=int(c1)
	# 	z=int(z)
	# 	#print z
	# 	#print uid + pw

	# 	csvfile=open('Signin.csv','r') 
	# 	csvreader=csv.reader(csvfile)# creating a csv reader object
	# 	fields=next(csvreader) 

	# 	for row in csvreader:
	# 		rows.append(row)
	# 	#rows=rows[0:]
	# 	print(rows)
	# 	y=-90
	# 	for data in rows :
	# 		if data[0]==uid:
	# 			y= data[1]
	# 			#print("w")
	# 			break
		
	# 	y=int(y)
	# 	T1=(y**c1)*(2**z)
	# 	T1=int(T1)
	# 	#print T1

	# 	inpu=str(y+T1+a)
	# 	inpu1=inpu.encode()
	# 	hash_object = hashlib.sha1(inpu1)
	# 	hex_dig = hash_object.hexdigest()
	# 	hsh=int(hex_dig,16)
	# 	c2=hsh%10
	# 	print(c1,c2)
	# 	if y==-90:
	# 		st='Wrong username,Please register'
	# 		byt=st.encode()
	# 		c.send(byt)
	# 	elif c2==c1:
	# 		st='Access Granted ,You have been successfully logged in'
	# 		byt=st.encode()
	# 		c.send(byt)
			
	# 	else :
	# 		st='The user_name or Password you entered is wrong'
	# 		byt=st.encode()
	# 		c.send(byt)
			



	# 	# extracting field names through first row 

	# 	# extracting each data row one by one 



	# elif (req==2):
	# 	st='Sign up'
	# 	byt=st.encode()
	# 	c.send(byt)
		
	# 	uid=c.recv(1024)
	# 	i=uid.decode()
	# 	pw=c.recv(1024)
	# 	pw.decode()

	# 	with open('Signin.csv', 'a') as newFile:
	# 		newFileWriter=csv.writer(newFile)
	# 		newFileWriter.writerow([uid, pw])
	# else:
	# 	print ('Invalid input ')





	# # send a thank you message to the client. 
	# st='\nThank you for connecting'
	# byt=st.encode()
	# c.send(byt)
	

	# # Close the connection with the client 
	# c.close() 