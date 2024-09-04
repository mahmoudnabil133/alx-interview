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
        ls = set(range(2, n + 1))
        role = 1
        while ls:
            prime = min(ls)
            ls.discard(prime)
            "remove prime and all multiples of prime"
            multiples = set(range(prime * 2, n + 1, prime))
            ls.difference_update(multiples)
            if not ls:
                if role == 1:
                    maria += 1
                else:
                    ben += 1
                break

            role *= -1
    print(maria, ben)

    if maria > ben:
        return "Maria"
    elif maria < ben:
        return "Ben"
    return None
