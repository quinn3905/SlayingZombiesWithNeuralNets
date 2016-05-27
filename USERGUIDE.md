Before you start using this project, make sure you have read INSTALLATION.md, installed all the necessary libraries, and placed all of our Python files (one if you are using the human version, three if you are using the Neural Network version) in the same folder.

#Human Version

Although the Neural Network version of "Zombie Slayer" is the focus of our project, it may be informative to experiment with the human version of the game in order to understand the task the Neural Network is trying to complete. To get started, just open "Zombie Slayer (Single Player).py". You will be prompted to choose how long you want the map to be (in ASCII squares), how many enemies (zombies) you want, and how many civilians you want. The game will then create a map with your specifications and ask for your move, as shown below:

!!!!!!!!!

Like the neural net, you may move your character ("P") in any direction with wasd, or enter "k" to use your knife to kill any zombies adjacent to you. Your objective is to kill all of the zombies before they zombify all of the civilians. At the end of the game, you will receive a score that indicates how well you did based on how many zombies you killed and how many civilians died---this is the same score that is used to determine how well the AI plays the game.

#Neural Network Version

###The Interface

Although there are three Python files for this version of the game, you should only open the one called "Zombie Slayer (Neural Network).py". So long as you have all three files in the same folder, this file will open the other ones automatically.