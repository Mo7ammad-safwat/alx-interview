#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    char = 'H'
    num = 0
    if n <= 1:
        return 0
    while len(char) < n:
        length = len(char)
        if length < n and n % length == 0:
            num += 1
            for i in range(length):
                char += char[i]
            num += 1
        else:
            char += 'H'
            num += 1
    return num
