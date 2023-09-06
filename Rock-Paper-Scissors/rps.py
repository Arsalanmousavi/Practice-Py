# Rock, Paper, Scissors

import random


def play_rps():

    moves = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'q': 'Quit'}
    possible_moves = list(moves.keys())

    print("Rock, Paper, Scissors")

    wins = 0
    losses = 0
    ties = 0

    print(f"{wins} wins, {losses} losses, {ties} ties")

    game = True

    while game:
        player_move = input(
            "\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit: ")

        if player_move in possible_moves:

            if player_move == "q":
                print(f"{wins} wins, {losses} losses, {ties} ties")
                break

            else:

                pc_move = random.choice(possible_moves[0:2])
                print(
                    f"{moves[player_move]} vs {moves[pc_move]}")

                if player_move == pc_move:
                    ties += 1
                    print("It's a Tie.")
                elif player_move == "r" and pc_move == "s" or \
                        player_move == "p" and pc_move == "r" or \
                        player_move == "s" and pc_move == "p":
                    wins += 1
                    print("It's a Win.")
                else:
                    losses += 1
                    print("It's a Loss.")

        else:
            print("bad input")
            continue


play_rps()
