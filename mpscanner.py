#multi threading port scanner
import socket
import threading #contains all the threading functionality of python
import queue

IP = '192.168.1.254'
q = queue.Queue() #works like a list, has functions that work hand in hand with threading
#the queue will contain all the port numbers we want to port scan, and the threads will grab each port from this list, and remove it from the queue

#Storing port numbers in our queue
for i in range(1, 444):
    q.put(i) #puts 1000 elements in the queue

def scan(): #this is the function all the threads will run
    while not q.empty(): #runs while the queue still has numbers
        port = q.get() #grabs the first number in the queue and remove it
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #socket object
            try:
                s.connect((IP,port)) #attempts to connect with the IP and port
                print(f'port {port} is open!') #
            except:
                pass #if the connection does not work, move to the next port in the queue
        q.task_done() #only jeezus knoes

#Create number of threads we want to use
for i in range(10):
    t = threading.Thread(target=scan, daemon=True)
    #when assigning a thread you need to assign it a function, or the job you want it to do
    #setting daemon to true will close all the other threads when our program exits, making sure they cause no problems
    t.start() #tells the threads to start the job/function

q.join() #makes sure all the tasks are tasks are done
#if the tasks are not done, any code below this statement will not be executed
print('finished')
