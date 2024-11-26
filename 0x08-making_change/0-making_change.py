#!/usr/bin/python3
"""
Technical interview questions
coin change
makeChange: return min coins required to make change
"""

def makeChange(coins, total):
    """create an the dp array"""
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)

    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    if dp[total] != total + 1:
        return dp[total]
    else:
        return -1
