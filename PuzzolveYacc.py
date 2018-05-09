import ply.yacc as yacc
from PuzzolveLex import tokens


environment = {}

def run(p): # still not implemented... this is our next step...
    print(p)
    global environment
    if type(p) == tuple :
        if p[0] == '+' : return run(p[1]) + run(p[2])
        elif p[0] == '-' : return run(p[1]) - run(p[2])
        elif p[0] == '*' : return run(p[1]) * run(p[2])
        elif p[0] == '/' : return run(p[1]) / run(p[2])
        elif p[0] == '%' : return run(p[1]) % run(p[2])
        elif p[0] == '=' :
            environment[p[1]] = run(p[2])
            print(environment[p[1]])
        elif p[0] == 'var' :
            if p[1] not in environment : return "UNDECLARED VARIABLE!"
            return environment[p[1]]
    else : return p


def p_eval(p): # May add more functions...
    '''
    eval : go_up
         | end_map
         | run_solution
         | set_traverse
         | go_down
         | exit_game
         | go_left
         | undo_move
         | build_map
         | build_solution
         | go_right
         | start_map
         | switch_map
         | set_obstacle
         | map_assign
         | solution_assign
         | edit_id
         | get_id
         | remove
         | replace_index
         | empty
    '''
    print(run(p[1]))

def p_go_up(p):
    '''
    go_up : MOVE UP
            | MOVE UP INT
            | MOVE UP LP INT RP
    '''
    try:
        p[0] = ('UP', p[4])
    except:
        try:
            p[0] = ('UP', p[3])
        except:
            p[0] = ('UP', 1)

def p_end_map(p):
    '''
    end_map : SET END AT INT
    '''
    p[0] = ('END', p[4])

def p_run_solution(p):
    '''
    run_solution : RUN ID
    '''
    p[0] = ('RUN', p[2])

def p_set_traverse(p):
    '''
    set_traverse : SET TRAVERSE TO INT INT
                 | SET TRAVERSE TO INT COMMA INT
                 | SET TRAVERSE TO LP INT COMMA INT RP
    '''
    try:
        p[0] = ('TRAVERSE', p[5], p[7])
    except:
        try:
            p[0] = ('TRAVERSE', p[4], p[6])
        except:
            p[0] = ('TRAVERSE', p[4], p[5])
def p_go_down(p):
    '''
    go_down : MOVE DOWN
            | MOVE DOWN INT
            | MOVE DOWN LP INT RP
    '''
    try:
        p[0] = ('DOWN', p[4])
    except:
        try:
            p[0] = ('DOWN', p[3])
        except:
            p[0] = ('DOWN', 1)

def p_exit_game(p): # NOTE THE RETURN...
    '''
    exit_game : EXIT
    '''
    p[0] = 'EXIT'

def p_go_left(p): # TODO -> Make sure that the run method accepts the same second parameter in the except...
    '''
    go_left : MOVE LEFT
            | MOVE LEFT INT
            | MOVE LEFT LP INT RP
    '''
    try:
        p[0] = ('LEFT', p[4])
    except:
        try:
            p[0] = ('LEFT', p[3])
        except:
            p[0] = ('LEFT', 1)

def p_undo_move(p): # NOTE THE RETURN...
    '''
    undo_move : UNDO
    '''
    p[0] = 'UNDO'

def p_build_map(p): # MUST TAKE CARE... Build Map & Build Solution are the same...
    '''
    build_map : BUILD ID
    '''
    p[0] = ('BUILD', p[2])

def p_build_solution(p): # needed???
    '''
    build_solution : BUILD ID
    '''
    p[0] = ('BUILD', p[2])

def p_go_right(p):
    '''
    go_right : MOVE RIGHT
            | MOVE RIGHT INT
            | MOVE RIGHT LP INT RP
    '''
    try:
        p[0] = ('RIGHT', p[4])
    except:
        try:
            p[0] = ('RIGHT', p[3])
        except:
            p[0] = ('RIGHT', 1)

def p_start_map(p):
    '''
    start_map : SET START AT INT
    '''
    p[0] = ('START', p[4])

def p_switch_map(p):
    '''
    switch_map : SWITCH TO ID
    '''
    p[0] = ('SWITCH', p[3])

def p_set_obstacle(p): # NOT FINISHED...
    '''
    set_obstacle : ADD ID AT INT INT
                 | ADD ID AT INT COMMA INT
                 | ADD ID AT LP INT COMMA INT RP
    '''
    try:
        p[0] = ('OBSTACLE', p[2], p[5], p[7])
    except:
        try:
            p[0] = ('OBSTACLE', p[2], p[4], p[6])
        except:
            p[0] = ('OBSTACLE', p[2], p[4], p[5])

def p_map_assign(p):
    '''
    map_assign : CREATE MAP NAMED ID
    '''
    p[0] = ('MAP', p[4])

def p_solution_assign(p):
    '''
    solution_assign : CREATE SOLUTION NAMED ID
    '''
    p[0] = ('SOLUTION', p[4])


def p_edit_id(p):
    '''
    edit_id : EDIT ID
    '''
    p[0] = ('EDIT', p[2])

def p_get_id(p):
    '''
    get_id : GET ID
    '''
    p[0] = ('GET', p[2])

def p_remove(p):
    '''
    remove : REMOVE INT
    '''
    p[0] = ('REMOVE', p[2])

def p_replace_index(p):
    '''
    replace_index : REPLACE ID ID
                  | REPLACE INT MOVE UP
                  | REPLACE INT MOVE DOWN
                  | REPLACE INT MOVE LEFT
                  | REPLACE INT MOVE RIGHT
                  | REPLACE INT MOVE UP INT
                  | REPLACE INT MOVE DOWN INT
                  | REPLACE INT MOVE LEFT INT
                  | REPLACE INT MOVE RIGHT INT
                  | REPLACE INT MOVE UP LP INT RP
                  | REPLACE INT MOVE DOWN LP INT RP
                  | REPLACE INT MOVE LEFT LP INT RP
                  | REPLACE INT MOVE RIGHT LP INT RP

    '''
    try:
        p[0] = ('REPLACE', p[2], p[4], p[6])
    except:
        try:
            p[0] = ('REPLACE', p[2], p[4], p[5])
        except:
            try:
                p[0] = ('REPLACE', p[2], p[4], 1)
            except:
                p[0] = ('REPLACE', p[2], p[3])

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    try:
        print("Oops! Error in: " + str(p.value))
    except:
        print("Oops! Unexpected Error. Try again.")



parser = yacc.yacc()

# The Scanner...
while True :

    try :
        line = input('> ')
    except EOFError : break
    parser.parse(line.lower())
