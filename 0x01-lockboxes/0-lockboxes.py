#!/usr/bin/python3
"game to itrerate rooms with keys"


def canUnlockAll(boxes):
    "check looked or unlocked"
    visited = set()
    def dfs(rooms, i):
        "recursion to each room"
        visited.add(i)
        for k in rooms[i]:
            if k not in visited:
                dfs(rooms, k)
    dfs(boxes, 0)
    for i in range(len(boxes)):
        if i not in visited:
            return False
    return True
