# ------------------------------------------------------------
# Puzzolve
# ------------------------------------------------------------

# Import parser to start execution
from PuzzolveYacc import parser


def main():
    while True:
        try:
            s = input('\nPuzzolve > ')
        except EOFError:
            break

        if s == 'exit':
            break
        if not s:
            continue # Empty input, keep scanning...

        parser.parse(s)

if __name__ == '__main__':
    main()