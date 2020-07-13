from collections import deque
from interpreters.utils import get_dict


def smallfuck_interpreter(code, tape):
    D = get_dict(code)
    pointer = 0
    tape = list(tape)
    i = 0
    stack = deque()

    while pointer >= 0 and pointer < len(tape) and i < len(code):
        cmd = code[i]

        if cmd == ">":
            pointer += 1

        elif cmd == "<":
            pointer -= 1

        elif cmd == "*":
            if tape[pointer] == "1":
                tape[pointer] = "0"
            else:
                tape[pointer] = "1"

        elif cmd == "[":
            if tape[pointer] == "0":
                i = D[str(i)]
            else:
                stack.append(i)

        elif cmd == "]":
            if tape[pointer] != "0":
                i = stack[-1]
            else:
                stack.pop()

        i += 1

    return "".join(tape)
