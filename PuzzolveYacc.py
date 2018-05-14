import ply.yacc as yacc
from PuzzolveLex import tokens
from GameController import Controller
import sys
global environment

c = Controller()
environment = {}
current_map = None
built_map = None # BOOLEAN... building map
built_sol = None # BOOLEAN... building solution
execution = True

# def run(p): # still not implemented... this is our next step...
#     print(p)
#     if type(p) == tuple :
#         print("tuple...")
#         if p[0] == 'EXIT' :
#             print("ne")
#             c.exit()
#         elif p[0] == 'END' : return #something
#         elif p[0] == 'RUN' : return #something
#         elif p[0] == 'TRAVERSE' : return #something
#         elif p[0] == 'UP' : return #something
#         elif p[0] == 'DOWN' : return #something
#         elif p[0] == 'LEFT' : return #something
#         elif p[0] == 'RIGHT' : return #something
#         elif p[0] == 'UNDO' : return #something
#         elif p[0] == 'BUILD' : return #something
#         elif p[0] == 'START' : return #something
#         elif p[0] == 'SWITCH' : return #something
#         elif p[0] == 'OBSTACLE' : return #something
#         elif p[0] == 'MAP' : # Create Map...
#             if(p[4] in environment):
#                 print("Oops! Map " + p[4] + " already exists.")
#             else :
#                 print(p[4])
#                 environment[p[4]] = c.create_map(p[4]) # TODO -> Implement...
#         elif p[0] == 'EDIT' : return #something
#         elif p[0] == 'GET' : return #something
#         elif p[0] == 'SOLUTION' : return #something
#         elif p[0] == 'REMOVE' : return #something
#         elif p[0] == 'REPLACE' : return #something
#     else : return p


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
    #print(run(p[1]))

def p_go_up(p):
    '''
    go_up : MOVE UP
            | MOVE UP INT
            | MOVE UP LP INT RP
    '''
    if(built_map  and built_sol == False):
        try:
            p[0] = ('UP', p[4])
        except:
            try:
                p[0] = ('UP', p[3])
            except:
                p[0] = ('UP', 1)
        c.move_up(p[0][1])
    else: print("Oops! Up can only be invoked while creating a solution.")

def p_end_map(p):
    '''
    end_map : SET END AT INT
    '''
    p[0] = ('END', p[4])
    if(built_map == False and built_sol == None):
        c.set_end(p[0][1])
    else: print("Oops! End can only be invoked while creating a map.")

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
    p[0] = p[1]
    if(p[1] == 'exit') :
        print("See you later!")
        c.exit()
        sys.exit()
    print("exit...")



def p_go_left(p): # TODO -> Make sure that the run method accepts the same second parameter in the except...
    '''
    go_left : MOVE LEFT
            | MOVE LEFT INT
            | MOVE LEFT LP INT RP
    '''
    if(built_map  and built_sol == False):
        try:
            p[0] = ('LEFT', p[4])
        except:
            try:
                p[0] = ('LEFT', p[3])
            except:
                p[0] = ('LEFT', 1)
        c.move_left(p[0][1])
    else: print("Oops! Left can only be invoked while creating a solution.")

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
    build_solution : BUILD SOLUTION ID
    '''
    p[0] = ('BUILD', p[2])
    if(built_map and built_sol == False):
        if(p[0][1] not in current_map.solutions):
            c.add_solution(current_map, p[0][1])
        else: print("Oops! Solution " + p[0][1] + " already exists in " + current_map.place()) # verify..
    else: print("Oops! Solutions can be built while in solution creation mode.")

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
    print("right ")

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
    if(built_map and (built_sol != False)):
        if(p[0][1] in environment):
            current_map = environment[p[0][1]]
            c.switch_map(p[0][1])
            print("Switched to " + p[0][1] + ".")
        else: print("Oops! " + p[0][1] + " has not been created.")
    else: print("Oops! Switch can only be performed while not in creation mode.")

def p_set_obstacle(p): # NOT FINISHED...
    '''
    set_obstacle : ADD ID AT INT INT
                 | ADD ID AT INT COMMA INT
                 | ADD ID AT LP INT COMMA INT RP
    '''
    if(built_map == False and built_sol == None):
        try:
            p[0] = ('OBSTACLE', p[2], p[5], p[7])
        except:
            try:
                p[0] = ('OBSTACLE', p[2], p[4], p[6])
            except:
                p[0] = ('OBSTACLE', p[2], p[4], p[5])
        c.add_obstacle(current_map, p[0][1], p[0][2], p[0][3])
        print(p[0][1] + " added.")
    else: print("Oops! Obstacles can only be added while creating a map.")

def p_map_assign(p):
    '''
    map_assign : CREATE MAP NAMED ID
    '''
    p[0] = ('MAP', p[4])
    if not ((built_map and built_sol == False) or (built_sol == None and built_map == False)): # NO>>>
        c.create_map(p[0][1])
        print("Creating " + p[0][1] + ".")
    else: print("Oops! Map can only be created while not in creation mode.")

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
    raise SyntaxError()

parser = yacc.yacc()

# The Scanner...
while True :
    try :
        line = input('Puzzolve >>> ')
    except EOFError : break
    try:
        parser.parse(line.lower())
    except SyntaxError as e: print(e.msg)
