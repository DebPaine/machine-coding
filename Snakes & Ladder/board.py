class Board:
    def __init__(self, size) -> None:
        self.size = size
        self.snakes = {}
        self.ladders = {}

    def add_snake(self, head, tail):
        self.snakes[head] = tail

    def add_ladder(self, bottom, top):
        self.ladders[bottom] = top

    def move_player(self, player, steps):
        new_position = player.position + steps
        if new_position > self.size:
            return (
                f"Player {player.name} didn't move as they would go outside the board!"
            )
        if new_position in self.ladders:
            player.position = self.ladders[player.position]
        if new_position in self.snakes:
            player.position = self.ladders[player.position]
        if player.position == self.size:
            return f"Player {player.name} is the winner!"
