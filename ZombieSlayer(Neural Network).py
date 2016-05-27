import random, time, math, socket, os

sideLen=eval(input("How long should one side of the map be?"))
enemyNum=eval(input("How many enemies do you want?"))
civNum=eval(input("How many civilians do you want?"))
theMap=[]

def printMap():
    for i in range(0,sideLen):
        for j in range(0,sideLen):
            print(theMap[i][j],end='')
        print('')

class Actor:
    name=""
    callsign=""
    location=[0,0]
    
    def randPlace(self):
        while True:
            self.location=[random.randint(0,sideLen-1),random.randint(0,sideLen-1)]
            if theMap[self.location[0]][self.location[1]]==" ":
                theMap[self.location[0]][self.location[1]]=self.callsign
                break
    def moveUp(self):
        if theMap[self.location[0]-1][self.location[1]]==" ": #If clear
            self.location=[self.location[0]-1,self.location[1]] #Change location
            theMap[self.location[0]][self.location[1]]=self.callsign #Print player there
            theMap[self.location[0]+1][self.location[1]]=" " #Erase old position

    def moveDown(self):
        if theMap[self.location[0]+1][self.location[1]]==" ": #If clear
            self.location=[self.location[0]+1,self.location[1]] #Change location
            theMap[self.location[0]][self.location[1]]=self.callsign #Print player there
            theMap[self.location[0]-1][self.location[1]]=" " #Erase old position

    def moveRight(self):
        if theMap[self.location[0]][self.location[1]+1]==" ": #If clear
            self.location=[self.location[0],self.location[1]+1] #Change location
            theMap[self.location[0]][self.location[1]]=self.callsign #Print player there
            theMap[self.location[0]][self.location[1]-1]=" " #Erase old position

    def moveLeft(self):
        if theMap[self.location[0]][self.location[1]-1]==" ": #If clear
            self.location=[self.location[0],self.location[1]-1] #Change location
            theMap[self.location[0]][self.location[1]]=self.callsign #Print player there
            theMap[self.location[0]][self.location[1]+1]=" " #Erase old position

    def knife(self):
        for i in range(-1,2):
            for j in range(-1,2):
                if theMap[self.location[0]+i][self.location[1]+j]=="E":
                    theMap[self.location[0]+i][self.location[1]+j]="D"
                    for k in enemyList:
                        if k.location==[self.location[0]+i,self.location[1]+j]:
                            enemyList.remove(k)
    def bite(self):
        for i in range(-1,2):
            for j in range(-1,2):
                if theMap[self.location[0]+i][self.location[1]+j]=="C":
                    theMap[self.location[0]+i][self.location[1]+j]="E"
                    for k in civilianList:
                        if k.location==[self.location[0]+i,self.location[1]+j]:
                            enemyList.append(k)
                            civilianList.remove(k)

def isnextto(self, direction, s):
    if(direction == "LEFT"):
        if(theMap[self.location[0]][self.location[1]-1] == s):
            return 1
        else:
            return 0
    elif(direction == "RIGHT"):
        if(theMap[self.location[0]][self.location[1]+1] == s):
            return 1
        else:
            return 0
    elif(direction == "UP"):
        if(theMap[self.location[0]-1][self.location[1]] == s):
            return 1
        else:
            return 0
    elif(direction == "DOWN"):
        if(theMap[self.location[0]+1][self.location[1]] == s):
            return 1
        else:
            return 0
    else:
        return 0

def findDistance(self1, self2):
    x1 = self1.location[1]
    y1 = self1.location[0]
    
    x2 = self2.location[1]
    y2 = self2.location[0]
    
    distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
    return distance

def findDx(self1,self2):
    x1 = self1.location[1]
    x2 = self2.location[1]
    
    distX = x2 - x1
    return distX

def findDy(self1,self2):
    y1 = self1.location[1]
    y2 = self2.location[1]
    
    distY = y2 - y1
    return distY

def findSmallest(self, a):
    try:
        temp = findDistance(self, a[0])
        nearest = a[0]
    except IndexError:
        return player #To keep the code from breaking when there's none of a type left, we just return the player.
    
        
    for j in a:
        temp2 = findDistance(self,j)
        if(temp2 < temp):
            temp = temp2
            nearest = j
    
    return nearest

os.startfile("ResultsPlotter.py") #Start the other two files!
os.startfile("NeuralNetwork.py")

host = socket.gethostname()  #Set the host to whatever the local machine's name is.
port = 12345 #Set the address to some random # (must be the same btwn. sender & receiver).

ping = socket.socket()  #Make a socket named ping. ("With" makes sure it's closed when we're done with it.
ping.bind((host,port)) #Give ping the address I came up with.
ping.listen(1) #Listen for connections to ping.
connection, addr = ping.accept()  #When a connection is accepted, we get a *new* socket, which I assign to "connection," plus the addr of the other party.
print("Connection established with",addr)
ping.close()


while True:
    for i in range(0,sideLen): #Assemble the list that will represent the map
        theMap.append(list([' ']*sideLen))

    for i in range(0,sideLen): #Create the walls of the map
        theMap[0][i]='X'
        theMap[i][0]='X'
        theMap[i][sideLen-1]='X'
        theMap[sideLen-1][i]='X'
        

##    for i in range(0,sideLen+2): #Create Random Obstacles
##        theMap[random.randint(1,sideLen-2)][random.randint(1,sideLen-2)]="X"
            

    player=Actor()
    player.callsign="P"
    player.randPlace()

    enemyList=[]
    for i in range(0,enemyNum):
        enemyList.append(0)
        enemyList[i]=Actor()
        enemyList[i].callsign='E'
        enemyList[i].randPlace()

    civilianList=[]
    for i in range(0,civNum):
        civilianList.append(0)
        civilianList[i]=Actor()
        civilianList[i].callsign='C'
        civilianList[i].randPlace()

    #printMap()

    

    points  = 0
    while True:       #Players and enemies move

        #Evaluate all the data to send to the NN.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        wallisAbove = isnextto(player, "UP", "X")  
        wallisBelow = isnextto(player, "DOWN", "X")
        wallisLeft = isnextto(player, "LEFT", "X")
        wallisRight = isnextto(player, "RIGHT", "X")

        nearEn = findSmallest(player, enemyList)
        nearEnX = findDx(player, nearEn)
        nearEnY = findDy(player, nearEn)

        nearCiv = findSmallest(player, civilianList)
        nearCivX = findDx(player, nearCiv)
        nearCivY = findDy(player, nearCiv)
        try:
            tempDang = findDistance(civilianList[0], enemyList[0])
            nearDang = civilianList[0]
        

            for j in civilianList:
                for i in enemyList:
                    tempDang2 = findDistance(i,j)
                    if(tempDang2 < tempDang):
                        tempDang = tempDang2
                        nearDang = j

            nearDangX = findDx(player, nearDang)
            nearDangY = findDy(player, nearDang)
        except IndexError:
            nearDangX = 1 #Set some meaningless values to prevent the code from breaking in this case.
            nearDangY = 1
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        data = [wallisAbove, wallisLeft, wallisRight, wallisBelow, nearCivX, nearCivY, nearEnX, nearEnY,nearDangX, nearDangY]
        for info in range(0,10):
            if data[info] < 0:
                #print(data[info])
                data[info] = data[info] + 256 #Convert every negative number to an 8 bit signed int.
                #print(data[info])

        connection.sendall(bytearray(data))
                           
        a = (connection.recv(4096)).decode('utf-8')
        if a=="a":
            player.moveLeft()

        elif a=="s":
            player.moveDown()

        elif a=="d":
            player.moveRight()

        elif a=="w":
            player.moveUp()

        elif a=="k":
            oldEnemy = len(enemyList)
            player.knife()
            newEnemy = len(enemyList)
            points = points + 5*(oldEnemy - newEnemy)
            #print(oldEnemy,newEnemy,points)

        wallisAbove = isnextto(player, "UP", "X")
        wallisBelow = isnextto(player, "DOWN", "X")
        wallisLeft = isnextto(player, "LEFT", "X")
        wallisRight = isnextto(player, "RIGHT", "X")
        
        for j in enemyList:
            a=random.randint(1,4)

            if a==1:
                j.moveLeft()

            elif a==2:
                j.moveDown()

            elif a==3:
                j.moveRight()

            elif a==4:
                j.moveUp()
                
            oldCivil = len(civilianList)
            j.bite()
            newCivil = len(civilianList)
            points = points - 10*(oldCivil - newCivil)
            #print(oldCivil,newCivil, points)
        
        for j in civilianList:
            a=random.randint(1,4)
            if a==1:
                j.moveLeft()

            elif a==2:
                j.moveDown()

            elif a==3:
                j.moveRight()

            elif a==4:
                j.moveUp()
        
        #printMap()
        
        if enemyList==[] or civilianList ==[]:
            points+= 10*civNum #This ensures that all scores are positive---losing all civs and killing no zombies is zero.
            sendData = [101,points]
            #print(sendData)
            connection.sendall(bytearray(sendData))
            break
        
                
##        nearEn = findSmallest(player, enemyList)
##        print("Nearest enemy is at ", nearEn.location[1], nearEn.location[0])
##
##        nearCiv = findSmallest(player, civilianList)
##        print("Nearest civilian is at ", nearCiv.location[1], nearCiv.location[0])
##
##         
##        tempDang = findDistance(civilianList[0], enemyList[0])
##        nearDang = civilianList[0]
##        
##        for j in civilianList:
##            for i in enemyList:
##                tempDang2 = findDistance(i,j)
##                if(tempDang2 < tempDang):
##                    tempDang = tempDang2
##                    nearDang = j
##        print("Civilian is at ", nearDang.location[1], nearDang.location[0], " is in danger")
        
    del theMap[:] #Reset the map, enemies, and civilians for the next game. It is important that this is OUTSIDE the previous loop, lest it be called every round.
    del enemyList[:]
    del civilianList[:]
