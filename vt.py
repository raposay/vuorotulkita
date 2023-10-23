import os, sys
import argparse

from enum import Enum


parser = argparse.ArgumentParser(
    prog="vt.py",
    description="Interprets transcripted logs between multiple parties!",
)

parser.add_argument('filename')# positional argument
parser.add_argument('-v', '--verbose', action='store_true')# on/off flag

class Node(Enum):
    
    member Punctuation(Enum):
        PERIOD = '.'
        EXCLAMATION = '!'
        QUESTION = '?'
        COMMA = ','
        DQUOTE = '"'
        QUOTE = '\''

    class Word:
        def __init__():
            self.word = ""

# An ordered list of Words or Punctuation
# contains count
class SubjectFeed:
    def __init__():
        # list of Node Objects
        # either Word, Punctuation, or Subject
        self.nodeList = []

# An ordered list of each Subject's individual feed
class Feed:
    def __init__():
        # list of SubjectFeed Objects
        # either Word, Punctuation, or Subject
        self.nodeList = []
    
    
if __name__ == "__main__":
    args = parser.parse_args()
    print(args.filename, args.count, args.verbose)
