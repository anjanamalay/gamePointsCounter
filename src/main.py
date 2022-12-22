import json
import player

print("Welcome to the game counter!")
print("------------------")
# print("If you like to play a new game enter new, else enter the name of your saved score card: ")
user_input = input("If you like to play a new game enter new, else enter the name of your saved score card: ")

game_name = ""
if user_input.lower() == "new":
    game_name = input("Enter your game name to save your scores: ")
else:
    game_name = user_input

score_card_name = user_input.lower() + ".json"

keep_going = True

num_players = int(input("How many players are there?: "))

players = []

for i in range(num_players):
    print("--------------------")
    print("Player", i, "enter your information: ")
    name = input("Name: ")
    p = player.Player(name, 0)
    players.append(p)
print("--------------------")

round = 0
while keep_going:
    print("---ROUND " + str(round) + " ---")
    
    for p in players:
        score = input(f"{p.name} please enter your score for this round: ")
        p.points += int(score)

    round+=1

    keep_going_str = input("Are you playing another round? Y/N: ")

    if keep_going_str == 'N':
        keep_going = False


print("Thanks for playing!")
print("Here are everyone's scores: ")
for p in players:
    print(p.name, "got", p.points, "points")
    


    
