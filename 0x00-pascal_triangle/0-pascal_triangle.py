
#!/usr/bin/python3
"""
0-pascal function that return 2d arr with each row of triangle
"""
def pascal_triangle(n):
    prev = []
    cur = [1]
    res = []
    for i in range(n):
        if prev:
            cur = []
            for j in range(len(prev)+1):
                one, two = 0, 0
                if j-1 >= 0 and j-1 < len(prev):
                    one = prev[j-1]
                if j >= 0 and j < len(prev):
                    two = prev[j]
                cur.append(one+two)
        prev = cur.copy()
        res.append(prev)
    return res
