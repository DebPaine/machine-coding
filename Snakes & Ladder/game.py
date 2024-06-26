from board import Board
from player import Player

import random


class Game:
    def __init__(self, board_size, players, snakes, ladders, dice_count=1) -> None:
        self.board = Board(board_size)
        self.dice = dice_count
        self.players = [Player(name) for name in players]
        for head, tail in snakes:
            self.board.add_snake(head, tail)
        for bottom, top in ladders:
            self.board.add_ladder(bottom, top)

    def roll_dice(self):
        return random.randint(1 * self.dice, 6 * self.dice)

    def player_turn(self, player):
        print(f"Player {player.name}'s turn")
        steps = self.roll_dice()
        print(f"Player {player.name} rolled a {steps}!")
        self.board.move_player(player)

    def start_game(self):
        while True:
            for player in self.players:
                self.player_turn(player)
