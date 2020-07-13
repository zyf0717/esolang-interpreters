from collections import deque
from interpreters.utils import get_bits, get_dict


def boolfuck_interpreter(code, string=""):
    bits = get_bits(string)
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
            if memory[pointer] > 1:
                memory[pointer] = 0

        elif cmd == ";":
            output = output + str(memory[pointer])

        elif cmd == ",":
            if j >= len(bits):
                memory[pointer] = 0
            else:
                memory[pointer] = int(bits[j])
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

    while len(output) % 8 != 0:
        output += "0"

    string_output = ""
    for i in range(0, len(output), 8):
        string_output += chr(int(output[i: i + 8][::-1], 2))

    return string_output
