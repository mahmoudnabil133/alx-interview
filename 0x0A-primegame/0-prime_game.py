#!/usr/bin/python3
"prime game"


def is_prime(n):
    "check if number is prime or not"
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    "check who is wenner maria or Ben"
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    players = [0, 'Maria', 'Ben']
    maria = 0
    ben = 0
    for n in nums:
        if n < 2:
            ben += 1
            continue
        ls = set()
        for i in range(2, n + 1):
            ls.add(i)

        start = 2
        role = 1
        while start <= n:
            player = players[role]
            pick = start
            while len(ls) >= 1 and pick <= n and is_prime(start):
                ls.remove(pick)
                pick *= 2

            if len(ls) == 0:
                if player == 'Maria':
                    maria += 1
                else:
                    ben += 1
                break

            start += 1
            if start not in ls:
                start += 1
            role = 3 - role

    if maria > ben:
        return "Maria"
    elif maria < ben:
        return "Ben"
    return None
