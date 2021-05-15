import othello
import random

class RandomPlayer:
    def __init__(self,seed = None):
        if seed:
            random.seed(seed)

    def optFor(board, turn):
        options = othello.optionsOf(board,turn)
        return random.choice(options)
