import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2 - 4):")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try again.")


max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:

    for player_index in range(players):
        print("\n Player number", player_index + 1, "turn has just started")
        print("Your total score:", players_score[player_index], '\n')


        currrent_score = 0
        while True:
            should_roll = input("Would you like to roll (y) ?")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1 ! Your turn is done!")
                currrent_score = 0
                break
            else:
                currrent_score += value
                print("You rolled a:", value)
            print("Your score is :", currrent_score)
        
        players_score[player_index] += currrent_score
        print("Your total score is:", players_score[player_index])


max_score = max(players_score)
winning_index = players_score.index(max_score)

print("Player number", winning_index + 1, "is the winner with a score of:", max_score)