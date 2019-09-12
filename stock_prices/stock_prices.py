#!/usr/bin/python

import argparse


def find_max_profit(prices):
    length = len(prices)
    #Not sure if using this variable is efficient.
    optimal_profit = -100000000
    for i in range(1, length):
        j = i + 1
        #Checks through all possible values and
        #compares to optimal_profit or continues looping
        while j < length:
            difference = prices[j] - prices[i]
            if difference > optimal_profit:
                optimal_profit = difference
            else:
                j += 1
    return optimal_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
