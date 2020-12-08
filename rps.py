import random


def rock_paper_scissor():
  """none --> none
  If you have no friend now you can play rock paper scissor by your self yeay!!!"""
    liste = ["rock", "paper", "scissor"]
    again = True
    while again:
        choix = input("rock, paper, scissor? ")
        enemy = random.choice(liste)
        if(choix == enemy):
            print(enemy, "equality")
        elif(choix == "rock" and enemy == "scissor"):
            print(enemy, "you win")
        elif(choix == "paper" and enemy == "rock"):
            print(enemy, "you win")
        elif(choix == "scissor" and enemy == "paper"):
            print(enemy, "you win")
        elif(choix == "scissor" and enemy == "rock"):
            print(enemy, "you lose")
        elif(choix == "rock" and enemy == "paper"):
            print(enemy, "you lose")
        elif(choix == "paper" and enemy == "scissor"):
            print(enemy, "you lose")
        result = input("again? (y, n): ")
        if result == "y":
            again = True
        else:
            again = False
rock_paper_scissor()
