Before you start using this project, make sure you have read INSTALLATION.md, installed all the necessary libraries, and placed all of our Python files (one if you are using the human version, three if you are using the Neural Network version) in the same folder.

#Human Version

Although the Neural Network version of "Zombie Slayer" is the focus of our project, it may be informative to experiment with the human version of the game in order to understand the task the Neural Network is trying to complete. To get started, just open "Zombie Slayer (Single Player).py". You will be prompted to choose how long you want the map to be (in ASCII squares), how many enemies (zombies) you want, and how many civilians you want. The game will then create a map with your specifications and ask for your move, as shown below:

!!!!!!!!!

Like the neural net, you may move your character ("P") in any direction with wasd, or enter "k" to use your knife to kill any zombies adjacent to you. Your objective is to kill all of the zombies before they zombify all of the civilians. At the end of the game, you will receive a score that indicates how well you did based on how many zombies you killed and how many civilians died---this is the same score that is used to determine how well the AI plays the game.

#Neural Network Version

###The Interface

Although there are three Python files for this version of the game, you should only open the one called "Zombie Slayer (Neural Network).py". Just like the single-player version of the game, this console window will ask you to choose the size of the map and number of zombies and civilians. After you have done so (as long as you have all three Python files in the same folder), this file will open the other ones automatically.

When this happens, you will have three black console windows and one gray "figure" window on the screen. The only ones that you need to watch are the figure window and the console window that looks like the one shown below:

!!!!!!!!!!!!

The figure window will show the performance of the neural networks over time as boxplots, while the console window will allow you to interact with the program.

###Options for Interacting

Our project provides you with many different ways to interact with and observe our neural networks! The first few prompts you will see in the console window will allow you to choose some of the parameters that determine how the genetic algorithm (GA) behind this project will function. You can choose whether the GA will "cross-over" the genomes of the neural networks during the evolution process (similar to sexual reproduction in nature) or not (as in asexual reproduction). You can also choose how likely it is that a given gene will mutate during evolution---higher values may speed up the evolution process, but they may also make it more erratic.

After this, you will be asked how many generations you want to "skip." This option allows you to tell the program to test a large number of neural networks as quickly as possible, so that you can see how the effects of your choices play out---OR (by entering "0") watch as every neural network is tested, viewing their individual scores, as well as the average score for their generation and how this differs from previous generations. Once the program has completed the number of generation you specified, you will be given this option again.

Finally, whenever the evolution process occurs (and the program is not skipping through generations) you will be given the option to watch this evolution "in detail." Choosing this option will make the program show you the individual scores of each member of the past generation, then walk you through the process of selecting parents, creating offspring, and mutating their genomes.

###Expected Behavior / Sample Results

The options that you choose with regard to crossing over and the mutation rate will have a large effect on the outcome you find. However, in most cases, the algorithm will improve dramatically in the beginning:

!!!!!!!!!!!

And then settle into a local optimum, which is usually either using the player's knife repeatedly, or using the knife interspersed with some movement in various directions. 

!!!!!!!!!!!

If you choose a sufficiently large map size, it is likely that after a sufficient number of generations the algorithm would begin to pursue the zombies actively. However, large map sizes can also become prohibitively computationally expensive.


###Troubleshooting / Known Issues

-> The Neural Network file may fail to make a socket connection to the other files the first time it is run on a new computer. The cause of this bug is unknown; the best fix is to leave the other two console windows running and re-open the Neural Network manually by clicking "NeuralNetwork.py"

-> If the program consistently fails to start, it is possible that it cannot find the libraries it needs. This is especially a problem on computers with multiple versions of Python installed, as the file may be attempting to use a version of Python that does not have the necessary libraries. The best fix (on Windows) is to run the program from the command line so that you can see which libraries are missing, and then double-check that the file is opening with the correct version of Python.

-> Once you have exceeded 50 generations, the stability of the figure window degrades. This is an issue with the matplotlib library and the underlying computational efficiency of Python, so the only fix is to use a more powerful computer.

-> If you find any other bugs, please create an "Open Issue" on this repository to let others know!
