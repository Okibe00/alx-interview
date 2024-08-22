#!/bin/python3

def makeChange(coins, total):
    """create an the dp array"""
    if total == 0:
        return 0

    dp = [total + 1] * (total + 1)

    '''initalize the starting position dp[0]'''
    dp[0] = 0

    '''loop through from 1 to total + 1
    this breaks the problem down to smaller chunks
    '''
    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    if dp[total] != total + 1:
        return dp[total]
    else:
        return -1
