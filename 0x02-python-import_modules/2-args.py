#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv) - 1
    if (arg == 0):
        print(f'{arg} arguments.')
    elif (arg == 1):
        print(f'{arg} argument:')
    else:
        print(f'{arg} arguments:')
    for i in range(arg):
        print(f'{i + 1}: {sys.argv[i + 1]}')
