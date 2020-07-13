def infinitick_interpreter(tape):
    index = 0
    pointer = 0
    memory = [0]
    output = ""

    while True:
        if index >= len(tape):
            index = 0

        cmd = tape[index]

        if cmd == ">":
            pointer += 1
            if pointer > len(memory) - 1:
                memory.append(0)
        elif cmd == "<":
            pointer -= 1
            if pointer < 0:
                memory = [0] + memory
                pointer = 0
        elif cmd == "+":
            memory[pointer] = memory[pointer] + 1
            if memory[pointer] > 255:
                memory[pointer] = 0
        elif cmd == "-":
            memory[pointer] = memory[pointer] - 1
            if memory[pointer] < 0:
                memory[pointer] = 255
        elif cmd == "*":
            output += chr(memory[pointer])
        elif cmd == "&":
            break
        elif cmd == "/":
            if memory[pointer] == 0:
                index += 1
        elif cmd == "\\":
            if memory[pointer] != 0:
                index += 1

        index += 1

    return output
