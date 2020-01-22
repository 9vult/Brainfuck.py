"""
bf.py
A Brainfuck interpreter
"""

import sys

"""
The main function
"""
def main():
    bffile = open(sys.argv[1], "r")
    program = bffile.read()
    bffile.close()
    
    pgrm_index = 0
    cells = [0]
    cell_index = 0

    while pgrm_index < len(program):
        command = program[pgrm_index]  # The current command

        if command == "+":  # Increment command
            cells[cell_index] += 1
            if cells[cell_index] >= 255:
                cells[cell_index] = 0

        elif command == "-":  # Decrement command
            cells[cell_index] -= 1
            if cells[cell_index] <= -1:
                cells[cell_index] <= 255

        elif command == ">":  # Move Right command
            cell_index += 1
            if len(cells) <= cell_index: 
                cells.append(0)

        elif command == "<":  # Move Left command
            cell_index -= 1

        elif command == "[":  # Right-hand loop identifier (start loop)
            if cells[cell_index] == 0:
                bracket_count = 1
                pgrm_index += 1
                while pgrm_index < len(program):
                    if program[pgrm_index] == "]" and bracket_count == 1:
                        break;
                    
                    if program[pgrm_index] == "[":
                        bracket_count += 1
                    elif program[pgrm_index] == "]":
                        bracket_count -= 1
                    
                    pgrm_index += 1

        elif command == "]":  # Left-hand loop identifier (end loop)
            if cells[cell_index] != 0:
                bracket_count = 1
                pgrm_index -= 1
                while pgrm_index >= 0:
                    if program[pgrm_index] == "[" and bracket_count == 1:
                        break;

                    if program[pgrm_index] == "[":
                        bracket_count -= 1
                    elif program[pgrm_index] == "]":
                        bracket_count += 1

                    pgrm_index -= 1
            
        elif command == ".":  # Print command
            print(chr(cells[cell_index]), end="")

        elif command == ",":  # Input command
            cells[cell_index] = ord(input(":")[0])

        pgrm_index += 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: bf.py [filename]")
    main()