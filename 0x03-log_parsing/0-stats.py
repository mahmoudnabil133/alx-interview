#!/usr/bin/python3
"log parse module"
import sys


def log_parse(file_size, status):
    "log parse"
    print(f"File size: {file_size}")
    for k, v in status.items():
        print(f"{k}: {v}")
file_size = 0
status = {}
count = 0

for l in sys.stdin:
    try:
        count += 1
        l = l.split(' ')
        file_size += int(l[-1][:-1])
        status[l[-2]] = status.get(l[-2], 0) + 1
        if count % 10 == 0:
            log_parse(file_size, status)
            status = {}
    except Exception as e:
        print('error')
        pass
