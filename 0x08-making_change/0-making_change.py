#!/usr/bin/python3
"make changes"


def makeChange(coins, total):
    "retuen min"
    if total <= 0:
        return 0
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
