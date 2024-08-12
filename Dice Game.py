import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
1

while True:
    players = input("Enter number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2 and 4")
    else:
        print("invalid input")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for player_index in range(players):
        print("\nPlayer", player_index + 1, " turn has started")
        print("Your total score is ", players_score[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled 1. Your turn is over!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled ", value)
                
            print("Your score is: ", current_score)

        players_score[player_index] += current_score
        print("Your total score is: ", players_score[player_index])


max_score = max(players_score)
winning_index = players_score.index(max_score)
print("The winner is player number ", winning_index + 1, "by a score of ", max_score)