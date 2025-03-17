# https://github.com/splitbrain/ook
# https://www.splitbrain.org/services/ook
# Brainfuck/Ook! Obfuscation/Encoding
def is_brainfuck(code):
    brainfuck_chars = {'>', '<', '+', '-', '.', ',', '[', ']'}
    is_brainfuck = all(c in brainfuck_chars or c.isspace() for c in code)
    if is_brainfuck:
        print("[SUCCESS] 检测到编码为 Brainfuck")
        print()
    return is_brainfuck
def decode_brainfuck(code):
    tape = [0] * 30000
    ptr = 0
    output = []
    i = 0
    while i < len(code):
        if code[i] == '>':
            ptr += 1
        elif code[i] == '<':
            ptr -= 1
        elif code[i] == '+':
            tape[ptr] += 1
        elif code[i] == '-':
            tape[ptr] -= 1
        elif code[i] == '.':
            output.append(chr(tape[ptr]))
        elif code[i] == ',':
            # For simplicity, we won't handle input in this example
            pass
        elif code[i] == '[':
            if tape[ptr] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    i += 1
                    if code[i] == '[':
                        open_brackets += 1
                    elif code[i] == ']':
                        open_brackets -= 1
        elif code[i] == ']':
            if tape[ptr] != 0:
                close_brackets = 1
                while close_brackets != 0:
                    i -= 1
                    if code[i] == '[':
                        close_brackets -= 1
                    elif code[i] == ']':
                        close_brackets += 1
        i += 1
    return ''.join(output)

def is_ook(code):
    ook_tokens = {'Ook. Ook?', 'Ook? Ook.', 'Ook. Ook.', 'Ook! Ook!', 'Ook! Ook.', 'Ook. Ook!', 'Ook! Ook?', 'Ook? Ook!', 'Ook? Ook?'}
    tokens = code.split()
    if len(tokens) % 2 != 0:
        print("length error")
        return False
    for i in range(0, len(tokens), 2):
        if f"{tokens[i]} {tokens[i+1]}" not in ook_tokens:
            print(f"{tokens[i]} {tokens[i+1]}")
            return False
    print("[SUCCESS] 检测到编码为 Ook")
    print()
    return True

def ook_to_brainfuck(ook_code):
    ook_to_bf = {
        'Ook. Ook?': '>',
        'Ook? Ook.': '<',
        'Ook. Ook.': '+',
        'Ook! Ook!': '-',
        'Ook! Ook.': '.',
        'Ook. Ook!': ',',
        'Ook! Ook?': '[',
        'Ook? Ook!': ']',
        'Ook? Ook?': 'n/a'
    }
    tokens = ook_code.split()
    bf_code = []
    for i in range(0, len(tokens), 2):
        bf_code.append(ook_to_bf[f"{tokens[i]} {tokens[i+1]}"])
    return ''.join(bf_code)
def decode_ook(ook_code):
    bf_code = ook_to_brainfuck(ook_code)
    return decode_brainfuck(bf_code)