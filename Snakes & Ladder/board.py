class Board:
    def __init__(self, size) -> None:
        self.size = size
        self.snakes = {}
        self.ladders = {}

    def add_snake(self, head, tail):
        if tail >= head:
            print("Did not add snake as tail of snake can't be equal or above head")
            return
        self.snakes[head] = tail

    def add_ladder(self, bottom, top):
        if bottom >= top:
            print("Did not add ladder as bottom of ladder can't be equal or above top")
            return
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
