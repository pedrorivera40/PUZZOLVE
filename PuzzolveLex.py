import ply.lex as lex


# Reserved words.
reserved = {

    'at' : 'AT',
    'to' : 'TO',
    'up': 'UP',
    'add' : 'ADD',
    'end': 'END',
    'get' : 'GET',
    'map': 'MAP',
    'run': 'RUN',
    'set': 'SET',
    'down': 'DOWN',
    'edit' : 'EDIT',
    'exit': 'EXIT',
    'left': 'LEFT',
    'move': 'MOVE',
    'undo': 'UNDO',
    'build': 'BUILD',
    'moves' : 'MOVES',
    'named': 'NAMED',
    'right': 'RIGHT',
    'start': 'START',
    'create' : 'CREATE',
    'remove' : 'REMOVE',
    'switch': 'SWITCH',
    'replace' : 'REPLACE',
    'obstacle' : 'OBSTABLE',
    'solution' : 'SOLUTION',
    'traverse' : 'TRAVERSE'

}

# List of token names.
tokens = [ 'COMMENT', 'INT', 'ID', 'LP', 'RP', 'COMMA' ] + list(reserved.values())

# Rule for user comments.
def t_COMMENT(t): # Comments shall be ignored...
    r'[#][^\n]*'
    pass


def t_INT(t):
    r'\d+' # INT corresponds to one or more consecutive occurrences an integer...
    t.value = int(t.value)
    return t

# Rule for reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Rule for left parenthesis.
t_LP = r'\('

# Rule for right parenthesis.
t_RP = r'\)'

# Rule for comma.
t_COMMA = r'\,'

# Error handling.
def t_error(t):
    print("Oops! Try again!")
    t.lexer.skip(1)

# Ignore spaces.
t_ignore = r' '


# Build the lexer.
lexer = lex.lex()