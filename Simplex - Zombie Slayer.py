
import random, time

sideLen=eval(input("How long should one side of the map be?"))
enemyNum=eval(input("How many enemies do you want?"))
civNum=eval(input("How many civilians do you want?"))
theMap=[]

for i in range(0,sideLen): #Assemble the list that will represent the map
    theMap.append(list([' ']*sideLen))



for i in range(0,sideLen): #Create the walls of the map
    theMap[0][i]='X'
    theMap[i][0]='X'
    theMap[i][sideLen-1]='X'
    theMap[sideLen-1][i]='X'
    

for i in range(0,sideLen+2): #Create Random Obstacles
    theMap[random.randint(1,sideLen-2)][random.randint(1,sideLen-2)]="X"
    

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


printMap()

while True:       #Players and enemies move
    a=input("Move?")
    if a=="a":
        player.moveLeft()

    elif a=="s":
        player.moveDown()

    elif a=="d":
        player.moveRight()

    elif a=="w":
        player.moveUp()

    elif a=="k":
        player.knife()

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
            
        j.bite()
            
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

    printMap()
    
    if enemyList==[]:
        print("Congratulations! You have won!")
        break

    if civilianList==[]:
        print("Oh no! You let all the civilians die!")
        break


time.sleep(2)

        





