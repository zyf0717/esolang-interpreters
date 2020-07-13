from interpreters.brainfuck import brainfuck_interpreter
from interpreters.boolfuck import boolfuck_interpreter
from interpreters.ticker import ticker_interpreter
from interpreters.infinitick import infinitick_interpreter
from interpreters.paintfuck import paintfuck_interpreter
from interpreters.smallfuck import smallfuck_interpreter


def start():
    print("""1. Ticker\n2. Infinitick\n3. Brainfuck\n4. Smallfuck\n5. Paintfuck\n6. Boolfuck""")
    language = int(input("Select interpreter: "))
    if language not in list(range(1, 7)):
        print("Invalid selection. Enter numbers 1-6 only.\n")
    else:
        code = input("Enter or paste code: ")
        output = ""
        if language == 1:
            output = ticker_interpreter(code)
        elif language == 2:
            output = infinitick_interpreter(code)
        elif language == 3:
            string = input("Enter input string (if any): ")
            output = brainfuck_interpreter(code, string)
        elif language == 4:
            tape = input("Enter or paste tape: ")
            output = smallfuck_interpreter(code, tape)
        elif language == 5:
            iterations = int(input("Enter number of iterations: "))
            width = int(input("Enter grid width: "))
            height = int(input("Enter grid height: "))
            output = paintfuck_interpreter(code, iterations, width, height)
        elif language == 6:
            output = boolfuck_interpreter(code)
        print()
        print("Output:", output)
        print()
    start()


if __name__ == "__main__":
    start()
