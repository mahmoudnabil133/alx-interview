#!/usr/bin/python3
""" calculate the perimeter of the island described in grid
"""


def island_perimeter(grid):
    "island perimeter"
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]:
                "check left border or water"
                if (j - 1 < 0) or not grid[i][j-1]:
                    perimeter += 1
                "check right border or water"
                if (j + 1 >= cols) or not grid[i][j + 1]:
                    perimeter += 1
                "check top border or water"
                if (i - 1 < 0) or not grid[i - 1][j]:
                    perimeter += 1
                "check bottom border or water"
                if (i + 1 >= rows) or not grid[i + 1][j]:
                    perimeter += 1
    return perimeter
