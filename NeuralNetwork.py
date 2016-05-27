import socket
import random
import copy
import time

e = 2.71828182845904523536 #Define euler's number.

oldGen = [] #The parent generation of neural nets
newGen = [] #The child generation of neurals nets
genScores = [] #The scores for each parent.
explicitEvolution = False
mutChance = 0.05
crossOver = True

for i in range(50): #Set up genScore to have length of 50.
    genScores.append(0)


def evolve():
    global oldGen, newGen, genScores

    if explicitEvolution == True:
        print("The current generation:")
        print("#    SCORE")
        for num in range(50):
            print(num,"   ",genScores[num])
        input("Press enter to continue...")
    if len(oldGen) > 0: #If there is an old generation to evolve from.
        
         for i in range(25): #Each iteration generates 2 creatures, so we perform it 25 times to get 50 creatures.
             

             choiceNum = random.randint(0,sum([i**3 for i in genScores])-1) #Choose a random number. Squaring makes higher-scoring NNs more likely to be selected.
             for j in range(50):
                 
                 choiceNum -= genScores[j]**3
                 if choiceNum<=0:
                     parent1 = oldGen[j] #By this process, we generate a random parent from oldGen, with prob proportional to score.
                     break #We only want one parent.
                    
             choiceNum = random.randint(0,sum([i**3 for i in genScores])-1) #Choose a random number.
             for j in range(50):
                 
                 choiceNum -= genScores[j]**3
                 if choiceNum<=0:
                     parent2 = oldGen[j] #Do the same process again to get parent2.
                     break #We only want one parent2.
             if crossOver ==True:
                 crossingPoint = random.randint(0,len(parent2.genome)) #Choose a random point at which to cross over parents' genes.
             else:
                 crossingPoint = 0
                 
             if explicitEvolution == True:
                 print("For the next two children,")
                 print("Parent #1 is Neural Net #",oldGen.index(parent1)," with score: ",genScores[oldGen.index(parent1)])
                 print("Parent #2 is Neural Net #",oldGen.index(parent2)," with score: ",genScores[oldGen.index(parent2)])
                 input("Press enter to continue...")
                 print("We are crossing these parents' genomes over at location ",crossingPoint)
                 print("Thus the first child we generate will get parent #1's genome up to ",crossingPoint, " and parent #2's genome past ",crossingPoint)
                 print("The second child will get the reverse.")
                 input("Press enter to continue...")

             

             childGenome1 = parent1.genome[crossingPoint:] + parent2.genome[:crossingPoint] #Cross over.
             childGenome2 = parent2.genome[crossingPoint:] + parent1.genome[:crossingPoint]

             if explicitEvolution == True:
                 print("Now it's time to mutate!")
             for gene in range(len(childGenome1)): #For each gene in the child
                if random.random() < mutChance: #On a five percent chance
                    childGenome1[gene] = ((random.random()*10)-5) #Mutate it.
                    if explicitEvolution == True:
                        print("Mutating the first child's genome at location ",gene)

             for gene in range(len(childGenome2)): #For each gene in the child
                if random.random() < mutChance: #On a five percent chance
                    childGenome2[gene] = ((random.random()*10)-5) #Mutate it.
                    if explicitEvolution == True:
                        print("Mutating the second child's genome at location ",gene)
            
             if explicitEvolution == True:
                 input("Press enter to continue...")
                 print("Children successfully added to the new generation!")
             newGen.append(brain(childGenome1)) #Create two newGen members with these newly evolved genomes.
             newGen.append(brain(childGenome2))

         oldGen = copy.deepcopy(newGen) #Now that we're done forming newGen, they become the parent generation.


         del newGen [:] #Clear the new generation.

         connection2.sendall(bytearray(genScores))  
         for score in range(len(genScores)):
            genScores[score] = 0 #Zero the scores.

         if explicitEvolution == True:
            print("EVOLUTION COMPLETE---RETURNING TO TESTING!")

    else: #If we're starting from scratch.
        for i in range(50):
            oldGen.append(brain(randomGenome())) #Make everything random.
            
    

def randomGenome():
    randGen = []
    for i in range(87):
        randGen.append((random.random()*10)-5) #Append a random number between -5 and 5
    return randGen


class neuron:
    def __init__(self):
        #NOTE: IT'S SUPER IMPORTANT TO HAVE THIS DUNDER because if I just defined weights, input, etc. in the general class,
        #then they would become CLASS attributes, and not INSTANCE attributes, so different neurons would not be able to have
        #different weights; it would all just point back to the class. I was able to get away with this in brain() because I
        #only had one brain. Now that I have multiple, I will define the attributes as instance attributes in __init__
        self.weights = []
        self.inputs = []
        self.bias = 1
        self.activation = 0

    def value(self): #If self.weights are the weights and self.inputs are the inputs, this returns output.
        self.activation = 0

        #print("Using the weights:",self.weights)
        #print("And the inputs:",self.inputs)
        for n in range(len(self.inputs)):
            #print("Old activation is ", self.activation)
            #print("We now add, ", self.weights[n]*self.inputs[n])
            self.activation += self.weights[n]*self.inputs[n]                
            #print("To get ",self.activation)

        #print("Finally, we have",self.activation)
        if self.activation - (10*self.bias) >=100:
            return 1.0
        elif self.activation - (10*self.bias) <=-100:
            return 0.0
        else:
            return 1/(1+e**((self.activation-(10*self.bias))*-1)) #Multiplying bias by 10 should make it more relevant.
    

class brain:


    def __init__(self, genome): #Uses the genome to build out weights and biases.
        self.entryNeurons = []
        self.secondaryInputs = []
        self.exitNeurons = []
        self.genome = genome #Accept a genome from the outside.
        for i in range(6):
            self.entryNeurons.append(0)
            self.entryNeurons[i] = neuron()
            for j in range(10):
                
                self.entryNeurons[i].weights.append(self.genome[(10*i+j)])
                

            self.entryNeurons[i].bias = self.genome[60+i]

        for i in range(3):
            self.exitNeurons.append(0)
            self.exitNeurons[-1] = neuron()
            for j in range(6):
                self.exitNeurons[i].weights.append(self.genome[66+6*i+j])
                #self.exitNeurons[i].inputs.append(0)

            self.exitNeurons[i].bias = self.genome[83+i]

    def result(self,rawInputs):
        

        del self.secondaryInputs[:] #We don't want to carry over inputs from previous iteration.
        
        for n in self.entryNeurons: #The inputs for the first level are the raw inputs
            n.inputs = rawInputs
            self.secondaryInputs.append(n.value()) #...and they yield these values
            #print(self.secondaryInputs)

        for n in self.exitNeurons:
            n.inputs = self.secondaryInputs #...which then become the inputs for the second layer.


        zero = self.exitNeurons[0].value()
        one = self.exitNeurons[1].value()
        two = self.exitNeurons[2].value()
        #print("ACTIVATION VALUES")
        #print(self.exitNeurons[0].activation)
        #print(self.exitNeurons[1].activation)
        #print(self.exitNeurons[2].activation)
        #print(self.exitNeurons[0].weights)
        #print(self.exitNeurons[0].inputs)

        if two>0.5: #If the neuron says knife, we knife.
            return "k"
        
        elif abs(zero-0.5)>= abs(one-0.5): #Otherwise, we determine which way to move based on the other exit neurons.
            if zero<0.5:
                return "a"
            else:
                return "d"

        else:
            if one<0.5:
                return "s"
            else:
                return "w"



def testNeuralNet(index):
    for trial in range(5):
        while True:
            recvdata = connection.recv(4096)
            
            data = list(recvdata)

            #print(data)
            if(data[0] == 101): #If we've won the game...
                
                genScores[n]+=data[1] #...add our score to our cumulative score.
                break #...and break the while True loop.
            else:
                for info in range(0,len(data)):
                    if data[info]>180:
                        data[info] = data[info] - 256 #Convert signed 8-bit ints back into normal negative ints.
                
            
            

                move = oldGen[index].result(data) #Get the move from our NN
                print("Move: ",move)
                connection.sendall(bytes(move,'utf-8')) #Send the move.
        


def report ():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("We are in generation #",generationNum)
    print("The running average score for this generation is: ",averageScore[generationNum])
    print("This is a change of ", (averageScore[generationNum]-averageScore[generationNum-1]), " from the previous generation.")
    print("Neural net #",n, " has been tested.")
    print("It received a score of ",genScores[n])

#MAKE A CONNECTION TO THE PLOTTER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
time.sleep(1) #Sleep just a little bit here to allow connections to be made.
host2 = socket.gethostname()
port2 = 11111

connection2 = socket.socket()  
connection2.connect((host2,port2)) #Make connection to the game.

print("Connection to plotter acheived.")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#MAKE A CONNECTION TO THE GAME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
host = socket.gethostname()
port = 12345

connection = socket.socket()  
connection.connect((host,port)) #Make connection to the game.

print("Connection to game acheived.")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



evolve()

generationNum = 0
averageScore = []
skip = 0

print("Let's setup how our Genetic Algorithm is going to work.")

crossyn = input("During the evolution process, would you like the genes of the two parents to 'cross over,' as in sexual reproduction (y/n)?")
if crossyn.upper() == "Y":
    crossOver = True
else:
    crossOver = False

mutChance = eval(input("Input a decimal between zero and one to determine how likely it is that any given gene will 'mutate' during the evolution process?"))

while True:
    if skip == 0:
        skip = eval(input("How many generations would you like to skip? (Type '0' to continue as normal.)  ::"))
        
    averageScore.append(0)
    
    for n in range(50):
        if skip == 0:
            proceed = input("Go on?")
        testNeuralNet(n)
        averageScore[generationNum] = sum(genScores)/(n+1)
        if skip == 0:
            report()
        
    if skip <2:
        print("ALL NEURAL NETWORKS TESTED. EVOLVING!")
        yn = input("Would you like to watch this evolution take place in detail (y/n)?")
        if yn.upper() == "Y":
            explicitEvolution = True
        else:
            explicitEvolution = False
    else:
        explicitEvolution = False
    evolve()
    generationNum+=1
    if skip>0:
        skip -= 1
    
    
     





    













    
