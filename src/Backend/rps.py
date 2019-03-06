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
def elimination(username, list):
    for i in list:
        if username == i:
            list.remove(username)
            return list
    return list


# a function to check if there is exactly 1 person remaining and returns that player as the winner
def winner(list):
    if len(list) == 1:
        return list[0] + " is the winner!"
    else:
        return str(len(list)) + " players remaining."
