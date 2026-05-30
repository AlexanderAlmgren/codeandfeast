def binarytodecimal(binary: str) -> int:

    # YOUR CODE GOES HERE

def decimaltobinary(decimal: int) -> str:

    # YOUR CODE GOES HERE

while True:
    try:
        line = input()

        if(len(line) == 8):
            print(binarytodecimal(line))

        else:
            print(decimaltobinary(int(line)))

    except EOFError:
        break

