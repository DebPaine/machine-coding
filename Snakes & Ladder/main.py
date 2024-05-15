"""
Requirements:
1. We need to have the following classes: board, players, dice, snakes, ladders
2. Board will have cells 1 to 100. We don't need to create a 2D array, we just need to see which
player reaches 100 first. 
3. We will need to generate a random no. between 1 to 6 for the dice.
4. There a few edge cases:
    a. At cell 100 (the end cell), there can't be a snake.
    b. There can't be an infinite loop where there is a snake and there is a ladder which form a loop.
    c. There can't be a snake and ladder start or end at the same cell.
     
"""

from game import Game


if __name__ == "__main__":
    # Get player names from input
    players = []
    player_count = int(input("Enter the no. of players playing"))
    for _ in range(player_count):
        players.append(input("Enter the player name"))

    # Get snakes positions from input
    snakes = []
    snakes_count = int(input("Enter the no. of snakes in the board"))
    for _ in range(snakes_count):
        head, tail = input("Enter the location of the snake's head and tail").split()
        snakes.append((int(head), int(tail)))

    # Get ladder positions from input
    ladders = []
    ladder_count = int(input("Enter the no. of ladder in the board"))
    for _ in range(ladder_count):
        top, bottom = input("Enter the location of the ladder's top and bottom").split()
        ladders.append((int(bottom), int(top)))

    game = Game(100, players, snakes, ladders, dice_count=1)
    game.start_game()
