import argparse

def check_braces(string):
    """
    A function that takes in a string and checks if braces are balanced.
    """
    BRACES = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    
    stack = []
    for char in string:
        if char in BRACES.values():
            stack.append(char)
        elif char in BRACES.keys():
            if stack == [] or BRACES[char] != stack.pop():
                return False
                
    return stack == []

def main(argv):
    with open(argv.input_file, 'r') as input_file:
        text = input_file.read()

    if check_braces(text):
        print("Braces are balanced.")
    else:
        print("Braces are not balanced.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Check brace balance.")
    parser.add_argument("input_file", help="Input file.")
    args = parser.parse_args()
    main(args)
