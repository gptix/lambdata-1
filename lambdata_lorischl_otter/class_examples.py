# Generate an example class for practice

from random import random


class Coinflips():
    """
    Simulates a heads/tails coinflip, with an option
    to change frequency of each
    """

    def __init__(self, rounds=0, heads_frequency=.5):
        self.rounds = rounds
        self.heads_frequency = heads_frequency
        self.tails = "Tails"
        self.heads = "Heads"

    def add_round(self):
        """
        Increase rounds by 1
        """
        self.rounds += 1

    def flip(self):
        """
        Generate flip outcome
        """
        return self.heads if random() <= self.heads_frequency else self.tails
