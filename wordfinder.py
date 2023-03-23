"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...
    
    def __init__(self, path):
        """Read dict and report #items read"""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Returns random word"""
        return random.choice(self.words)
