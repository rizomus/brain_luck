
def brain_luck(code, program_input):

    code = list(code)
    program_input = [int(ord(ch)) for ch in program_input]
    pointer = 0
    tape = [0 for x in range(2000)]
    output = ''
    i = 0

    while i < len(code):
        com = code[i]
        if com == '>':
            pointer +=1
            i += 1
        elif com == '<':
            pointer -= 1
            i += 1
        elif com == '+':
            tape[pointer] += 1
            if tape[pointer] == 256:
                tape[pointer] = 0
            elif tape[pointer] == -1:
                tape[pointer] = 255
            i += 1
        elif com == '-':
            tape[pointer] -= 1
            if tape[pointer] == 256:
                tape[pointer] = 0
            elif tape[pointer] == -1:
                tape[pointer] = 255
            i += 1
        elif com == '.':
            val = tape[pointer] 
            output += chr(val)
            i += 1
        elif com == ',':
            tape[pointer] = program_input.pop(0)
            i += 1
        elif com == '[':
            if tape[pointer] == 0:
                bracket = 1
                while bracket !=0:
                    i += 1
                    if code[i] == ']':
                        bracket -= 1
                    elif code[i] == '[':
                        bracket += 1
                i += 1
            else:
                i += 1
        elif com == ']':
            if tape[pointer] != 0:
                bracket = 1
                while bracket !=0:
                    i -= 1
                    if code[i] == '[':
                        bracket -= 1
                    elif code[i] == ']':
                        bracket += 1
                i += 1
            else:
                i += 1
    return output
