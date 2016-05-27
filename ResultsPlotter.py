import socket, time

#import sys
#sys.path.append('E:\\WinPython\\python-3.4.4.amd64\\Lib\\site-packages')
#print(sys.path)
myList = []

import matplotlib.pyplot as plt
import matplotlib.animation as anim


host = socket.gethostname()  #Set the host to whatever the local machine's name is.
port = 11111 #Set the address to some random # (must be the same btwn. sender & receiver).

with socket.socket() as ping:  #Make a socket named ping. ("With" makes sure it's closed when we're done with it.
    ping.bind((host,port)) #Give ping the address I came up with.
    ping.listen(1) #Listen for connections to ping.
    connection, addr = ping.accept()  #When a connection is accepted, we get a *new* socket, which I assign to "connection," plus the addr of the other party.
    print("Connection acheived! Waiting for data to plot!")


joe = plt.figure() #Create a figure named Joe
evoPlot = joe.add_subplot(1,1,1) #Create a plot on that figure named Joe

def update(i): #We occasionally want to update Joe by...
    recvdata = connection.recv(4096) #...getting new data
    myList.append(list(recvdata)) #...adding it to myList
    if len(myList) >50:
        del myList[0]
    evoPlot.clear() #...clear the old info off of evoPlot, and...
    evoPlot.boxplot(myList)#...and finally plotting that stuff out.

def initializer():
    evoPlot.boxplot([[0,0,0]])
    
j = anim.FuncAnimation(joe, update, init_func=initializer)
plt.show()

#plt.ion()
##while True:
##    print(myList)
##    recvdata = connection.recv(4096)
##    myList.append(list(recvdata))
##
##    plt.ion()
##    plt.boxplot(myList)
##    plt.show()
##    plt.close()
##plt.figure()
##
##def addToList(b):
##    myList.append(b)
##    
##def plotList(a):
##    plt.boxplot(a)
##
##
##plotList(myList)
##plt.show()
