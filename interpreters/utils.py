from copy import deepcopy
from collections import OrderedDict


def get_dict(code):
    D = dict()
    for i in range(len(code)):
        if code[i] == "[":
            D[str(i)] = None
        elif code[i] == "]":
            D[[(k) for k, v in D.items() if v is None][-1]] = i
    return D


def get_grid(width, height):
    row = [[0] * width]
    grid = []
    for _ in range(height):
        grid += deepcopy(row)
    return grid


def get_string(grid):
    return "\r\n".join("".join(str(x) for x in y) for y in grid)


def get_bits(string):
    output = ""
    for char in string:
        bits = bin(ord(char))[2:][::-1]
        while len(bits) < 8:
            bits += "0"
        output += bits
    return output
