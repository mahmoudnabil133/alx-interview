#!/usr/bin/python3
"nqueens problem"
import sys

if len(sys.argv) > 2 or len(sys.argv) == 1:
    print('Usage: nqueens N')
    sys.exit(1)

if not sys.argv[1].isdigit():
    print('N must be a number')
    sys.exit(1)

n = int(sys.argv[1])
if n < 4:
    print('N must be at least 4')
    sys.exit(1)

cols = set()
posDiag = set()
negDiag = set()

res = []
board = []


def backtrack(r):
    "backteck function"
    if r == n:
        res.append(board.copy())
        return

    for c in range(n):
        if c in cols or r-c in negDiag or r+c in posDiag:
            continue
        cols.add(c)
        negDiag.add(r-c)
        posDiag.add(r+c)
        board.append([r, c])

        backtrack(r+1)
        cols.remove(c)
        negDiag.remove(r-c)
        posDiag.remove(r+c)
        board.remove([r, c])


backtrack(0)

for result in res:
    print(result)
