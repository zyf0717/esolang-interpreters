from collections import deque
from interpreters.utils import get_dict, get_grid, get_string


def paintfuck_interpreter(code, iterations, width, height):
    D = get_dict(code)
    memory = get_grid(width, height)
    x = 0
    y = 0
    i = 0
    j = 0
    stack = deque()

    while i < len(code) and j < iterations:
        cmd = code[i]
        if cmd == "n":
            x -= 1
            if x < 0:
                x = height - 1
        elif cmd == "s":
            x += 1
            if x == height:
                x = 0
        elif cmd == "e":
            y += 1
            if y == width:
                y = 0
        elif cmd == "w":
            y -= 1
            if y == -1:
                y = width - 1
        elif cmd == "*":
            memory[x][y] += 1
            if memory[x][y] > 1:
                memory[x][y] = 0
        elif cmd == "[":
            if memory[x][y] == 0:
                i = D[str(i)]
            else:
                stack.append(i)
        elif cmd == "]":
            if memory[x][y] != 0:
                i = stack[-1]
            else:
                stack.pop()
        else:
            i += 1
            continue

        j += 1
        i += 1

    return get_string(memory)
