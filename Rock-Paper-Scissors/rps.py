# Rock, Paper, Scissors

import random

moves = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'q': 'Quit'}
possible_moves = list(moves.keys())


print("Rock, Paper, Scissors")

Wins = 0
Losses = 0
Ties = 0

print(f"{Wins} Wins, {Losses} Losses, {Ties} Ties")

game = True

while game:
    player_move = input(
        "\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit: ")

    if player_move in possible_moves:

        if player_move == "q":
            print(f"{Wins} Wins, {Losses} Losses, {Ties} Ties")
            break

        else:

            pc_move = random.choice(possible_moves[0:2])
            print(
                f"{moves[player_move]} vs {moves[pc_move]}")

            if player_move == pc_move:
                Ties += 1
                print("It's a Tie.")
            elif player_move == "r" and pc_move == "s" or \
                    player_move == "p" and pc_move == "r" or \
                    player_move == "s" and pc_move == "p":
                Wins += 1
                print("It's a Win.")
            else:
                Losses += 1
                print("It's a Loss.")

    else:
        print("bad input")
        continue
