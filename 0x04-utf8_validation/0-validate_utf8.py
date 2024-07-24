#!/usr/bin/python3
"""
check utf-8 vallidation of data
return True if valid otherwise false
"""


def validUTF8(data):
    """
    check if data is
    valid or not
    """

    for n in data:
        if n < 0 and n > 256:
            return False
    return True
