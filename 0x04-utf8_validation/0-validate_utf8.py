#!/usr/bin/python3
"""
check utf-8 vallidation of data
return True if valid otherwise false
utf-8 rules

for:

1-byte:
    0xxxxxxx
2-byte:
    110xxxxx 10xxxxxx
3-byte:
    1110xxxx 10xxxxxx 10xxxxxx
4-byte:
    11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
"""


def validUTF8(data):
    """
    check if data is
    valid or not
    """
    "check validation of the bytes after first byte in the character"

    msb1 = 1 << 7
    msb2 = 1 << 6
    num_of_bytes = 0
    for byte in data:
        msb = 1 << 7

        "started a new character"
        if num_of_bytes == 0:
            """
            determine number of bytes
            this character should be from
            the first byte
            """
            while msb & byte:
                num_of_bytes += 1
                msb >>= 1
            "if number of bytes is 0 then character is single byte"
            if num_of_bytes == 0:
                continue
            "character should less than 4 bytes"
            if num_of_bytes == 1 or num_of_bytes > 4:
                return False
        else:
            "byte should be 10xxxxxx"
            if not (msb1 & byte and not msb2 & byte):
                return False
        num_of_bytes -= 1

    return num_of_bytes == 0
