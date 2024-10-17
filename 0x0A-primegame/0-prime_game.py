#!/usr/bin/python3
'''prime game

'''


def sieve_of_eratosthenes(max_n):
    '''create  a list of prime numbers
    '''
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(max_n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False
    return is_prime


def count_prime_moves(n, primes):
    '''select a number from the current round
    '''
    remaining = [True] * (n + 1)
    prime_moves = 0

    for p in range(2, n + 1):
        if primes[p] and remaining[p]:
            prime_moves += 1
            for multiple in range(p, n + 1, p):
                remaining[multiple] = False

    return prime_moves


def isWinner(x, nums):
    if not nums or x == 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_moves = count_prime_moves(n, primes)
        if prime_moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
