from collections import deque
from interpreters.utils import get_dict


def brainfuck_interpreter(code, string=""):
    D = get_dict(code)
    memory = [0]
    pointer = 0
    output = ""
    i = 0
    j = 0
    stack = deque()

    while i < len(code):
        cmd = code[i]

        if cmd == ">":
            pointer += 1
            if pointer > len(memory) - 1:
                memory.append(0)

        elif cmd == "<":
            pointer -= 1
            if pointer < 0:
                memory.insert(0, 0)
                pointer = 0

        elif cmd == "+":
            memory[pointer] += 1
            if memory[pointer] > 255:
                memory[pointer] = 0

        elif cmd == "-":
            memory[pointer] -= 1
            if memory[pointer] < 0:
                memory[pointer] = 255

        elif cmd == ".":
            output += chr(memory[pointer])

        elif cmd == ",":
            memory[pointer] = ord(string[j])
            j += 1

        elif cmd == "[":
            if memory[pointer] == 0:
                i = D[str(i)]
            else:
                stack.append(i)

        elif cmd == "]":
            if memory[pointer] != 0:
                i = stack[-1]
            else:
                stack.pop()

        i += 1

    return output
