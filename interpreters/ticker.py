def ticker_interpreter(tape):
    pointer = 0
    memory = [0]
    output = ""
    for cmd in tape:
        if cmd == ">":
            pointer += 1
        elif cmd == "<":
            pointer -= 1
        elif cmd == "*":
            if pointer >= 0 and pointer < len(memory):
                output += chr(memory[pointer])
            else:
                output += chr(0)
        elif cmd == "+" and pointer >= 0 and pointer < len(memory):
            memory[pointer] = memory[pointer] + 1
            if memory[pointer] > 255:
                memory[pointer] = 0
        elif cmd == "-" and pointer >= 0 and pointer < len(memory):
            memory[pointer] = memory[pointer] - 1
            if memory[pointer] < 0:
                memory[pointer] = 255
        elif cmd == "/" and pointer >= 0 and pointer < len(memory):
            memory[pointer] = 0
        elif cmd == "!":
            memory.append(0)
    return output
