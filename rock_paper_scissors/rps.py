#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # Shows all the possible moves that the user can
    # make. Order of moves based on the initial value of 1st: rock 2nd: paper 3rd: scissor.
    # Cache
    # 0 being being no moves
    # 1 essentially playing by yourself.
    moves = ["rock", "paper", "scissors"]
    cache = {
        0: [[]],
        1: [["rock"], ["paper"], ["scissors"]]
    }

    def recurse(n):
      #Check to see if those cases above are
      #are what the user is looking for.
        if n in cache:
            return cache[n]

        # Appending is happening here with the cache.
        # r is the preceding cache before it with m being tagged on
        # in the order of [rock paper scissor].
        # Example n = 2. (n = 1) = [["rock"], ["paper"], ["scissors"]]
        # m is appended to (n = 1)
        # m is bracketed for list addition. 
        cache[n] = [r + [m] for r in recurse(n - 1) for m in moves]

        return cache[n]

    return recurse(n)


print(rock_paper_scissors(5))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
