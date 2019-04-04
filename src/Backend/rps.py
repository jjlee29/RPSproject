import time
import random
# a function to check if the player chooses rock, paper, or scissor
def pickRPS(username, playerChoice):
    list = ["rock", "paper", "scissor"]
    for i in list:
        if playerChoice == "i[0]":
            playerChoice = "rock"
            return username + " chooses " + playerChoice + "."
        elif playerChoice == "i[1]":
            playerChoice = "paper"
            return username + " chooses " + playerChoice + "."
        elif playerChoice == "i[2]":
            playerChoice = "scissor"
            return username + " chooses " + playerChoice + "."
    return "Did not choose in time."


# a function that takes a username and removes them from a list of active players
def elimination(username, listOfPlayers):
    for i in listOfPlayers:
        if username == i:
            listOfPlayers.remove(username)
            return listOfPlayers
    return listOfPlayers


# a function to check if there is exactly 1 person remaining and returns that player as the winner
def winner(listOfPlayers):
    if len(listOfPlayers) == 1:
        return listOfPlayers[0] + " is the winner!"
    else:
        return str(len(listOfPlayers)) + " players remaining."


# a function that starts a timer of 30 seconds before starting the game once at least 8 people have joined the lobby
def timer(listOfPlayers):
    seconds = 30
    while len(listOfPlayers) >= 8 and seconds > 1:
        print(str(seconds) + " seconds remaining until game starts.")
        time.sleep(1)
        seconds -= 1
        if seconds == 1:
            print(str(seconds) + " second remaining until game starts.")
            time.sleep(1)
            seconds -= 1
        if seconds == 0:
            print("Start Game!")
            return "Start Game!"


# a function that chooses what the computer picks
def compChoice(computerChoice):
    bot = random.randint(0, 2)
    if bot == 0:
        computerChoice == "rock"
        return "Computer chooses " + computerChoice + "."
    elif bot == 1:
        computerChoice == "paper"
        return "Computer chooses " + computerChoice + "."
    elif bot == 2:
        computerChoice == "scissors"
        return "Computer chooses " + computerChoice + "."


# a function compares what the computer chooses with the player's choice
def comparator(username, playerChoice, computerChoice):
    if playerChoice == "rock" and computerChoice == "paper":
        return "Paper covers " + playerChoice + ". " + "Computer wins."
    elif playerChoice == "rock" and computerChoice == "scissors":
        return "Rock crushes " + computerChoice + ". " + username + " wins."
    if playerChoice == "paper" and computerChoice == "scissors":
        return "Scissors cuts " + playerChoice + ". " + "Computer wins."
    elif playerChoice == "paper" and computerChoice == "rock":
        return "Paper covers " + computerChoice + ". " + username + " wins."
    if playerChoice == "scissors" and computerChoice == "rock":
        return "Rock crushes " + playerChoice + ". " + "Computer wins."
    elif playerChoice == "scissors" and computerChoice == "paper":
        return "Scissors cuts " + computerChoice + ". " + username + " wins."
    if playerChoice == computerChoice:
        return "Draw!"


# a function that adds a username to a list of players playing in the same bracket
def playerList(username, listOfPlayers):
    listOfPlayers.append(username)