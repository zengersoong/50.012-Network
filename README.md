# Network Labs #2
Network 50.012 Mod ISTD Term 6

Lab 2:Building your own web application with a Restful API

### List of task to fulfil for Lab
1. This lab we are tasked to write a simple web server using restful API
2. Server and client side have to be able to receive and send JSON datastructures respectively
3. Should contain at least 5 different API calls/ways to interact with your API
4. At least two nouns and different verbs(GET/PUT/DELETE)
5. Implement a simple HTTP authentication with a username and a password. - No Need to implement HTTPS/TLS YET


### My lab strategy is a set up a simple way for students to view their assigned student ID or username and 
A server-client web server for admins to access the MongoDB to make changes and alteration to the student ID/username using flask.  
*MongoDB + Python Flask + RESTFUL API*

# Directory/ Container Nouns
1. /student
2. /admin
3. /login

# Methods
1. GET
2. POST
3. PUT
4. DELETE
5. NOTICE

# Server Functions / Client curl 
1. one_of_student() -
This is for students to
access the mongodb
and get their student
id. (json or plaintext)  
__*`curl -H "Content-
Type:text/plain" -X
GET -d "test" http://
127.0.0.1:5000/student`*__  or   __*`Curl - H”Content-
Type: application/
json” -X GET -d
“{“name”: “test”}”'
http://127.0.0.1:5000/
student`*__

2. get_all_students()-
This is for admin
(after login function),
returns all students in
MongoDB in json
format.  
__*`curl -X GET http://
127.0.0.1:5000/admin`*__ 

3. add_student()-
This function is used
for admins to add a
student by sending a
json file with the
student id and
password of the
student, to be saved in
MongoDB   
__*`curl -H "Content-
Type: application/
json" -X POST -d
‘{"student":"test" ,
"studentId" :
"234235" }' http://
127.0.0.1:5000/admin`*__

4. Authenticate()-
This function is for
admins to login to
access admin-only
functions, under /
admin containers.  
__*`curl -H "Content-
Type: application/
json" -X POST -d
'{"username":"iamfast"
, "password" :
"checkmeoff" }' http://
127.0.0.1:5000/login`*__

5. alterationId(): -
This function is used for
admins to edit a student’s
ID by searching their
name up on MongoDB
and updating it.'  
__*`curl -H "Content-Type:
application/json" -X
PUT -d '{"name":"test" ,
"studentId" : "777" }'
http://127.0.0.1:5000/
admin`*__

6. delete_All(): -
This function is used for
admins to delete all
students in the MongoDB  
__*`curl -X DELETE
http://127.0.0.1:5000/
admin`*__

7. delete_student(name):
This is for admins to
delete users as indicated
in the path name.  
__*`curl -X DELETE
http://127.0.0.1:5000/
admin/test`*__


8. notice():-
Just a simply notice
board showing things like
instruction  
__*`curl -X NOTICE
http://127.0.0.1:5000/
student`*__


### How to run?
1. Download python3
2. Get the libraries required such as `pip3 install flask` && `sudo pip3 install pymongo`
3. Open up two terminals, Command prompt on either Linux-based operating system / macOS
4. Run `python3 week2lab2.py` to start the server up.
5. On the other terminal run the respective curl commands.


## References and guides used
1. https://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php
2. https://flask-pymongo.readthedocs.io/en/latest/
3. http://flask.pocoo.org/docs/0.12/installation/




# Network Labs #3
Network 50.012 Mod ISTD Term 6
Lab 3:Server and Client UDP   
Instructor(s): Prof Jit Biswas 
### List of task to fulfil for Lab
1. The client should send approximately 1.5Mbps
2. No packets should be dropped by default
3. If we increase the packet rate by 10%, we should see dropped packets
4. The server should report if incoming traffic has dropped datagrams



### My lab strategy 
Absolutely no strategy , just send and wait to ensure that packets are sent at 1.5Mbps to server.
Json is used to keep track of segment IDs, a python list is kept to keep track of which segment are late/ dropped.

# Network Labs #4
Network 50.012 Mod ISTD Term 6
Lab 4: BGP routing  
Instructor(s): Prof Jit Biswas 
1. Discovering more about mininet and learning the basics
2. Getting familiar with BGP and Zebra tools
3. Understanding malicious BGP abuse

# Network Labs #5
Network 50.012 Mod ISTD Term 6
Lab 5: Designing and implementing a small network    
Instructor(s): Prof Jit Biswas 
1. Use knowledge from the class to design and implement a small network
2. Once again, we are using mininet to run a set of virtualized hosts
3. Your job is to connect these hosts correctly through switches and routers, and to configure
critical services
4. Changing DHCP configuration
5. Configuring DNS
6. Observing NAT
7. Creating a simple firewalling by setting up iptables
  1. Changing iptable routing
  2. https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/

# Network Labs #10
Network 50.012 Mod ISTD Term 6
### Software Defined Networks Basics
Instructor(s): Prof Jit Biswas 
Date: 30/11/18  
#### Overview
• In this exercise, we will use mininet to write a simple SDN controller to manage a set of
switches.
• Software-Defined Networking (SDN) is a promising new approach to network management
• We have linked a nice video intro to SDN in eDimension
• We start by using OpenFlow and the POX controller to make a SDN switch learn mac addresses
(similar to the cam table in a normal non-SDN switch)
• We then extend the controller to install specific flows in the switch
• This exercise is built on the official mininet tutorial at https://github.com/mininet/
openflow-tutorial/wiki/Create-a-Learning-Switch
#### Setup
• During the setup, you should be connected to SUTD_Student to have Internet access.
• This exercise requires a working mininet setup. All lab machines have this running already
#### POX
• Install the POX SDN controller into a directory of your choice (e.g., ~/lab10/pox)
#### Installing flow table entries in the switch
• Example. Create a flow_mod that sends packets from port 3 out of port 4.
