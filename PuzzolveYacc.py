import ply.yacc as yacc
from PuzzolveLex import tokens
from GameController import Controller
import sys
from Grid import Grid
global environment

c = Controller()
environment = {}
current_map = Grid.Grid("land") # NONE
current_solution = 'la' # NONE
built_map = None # BOOLEAN... building map
built_sol = None # BOOLEAN... building solution
execution = True

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
         | empty
    '''
    print(p[0])

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
        if(current_map.add_move(current_solution, p[0])):
            c.move_up(p[0])
        else : print("Oops! Solution does not exist.")
    else: print("Oops! Up can only be invoked while creating a solution.")

def p_end_map(p):
    '''
    end_map : SET END AT INT INT
    '''
    p[0] = ('END', p[4], p[5])
    if(built_map == False and built_sol == None):
        c.set_end(p[4], p[5])
    else: print("Oops! End can only be invoked while creating a map.")

def p_run_solution(p):
    '''
    run_solution : RUN ID
    '''
    p[0] = ('RUN', p[2])
    if (built_map and built_sol and (current_map != None)):
        if(p[0][1] in current_map.solutions):
            c.run_solution(current_map.solutions[p[0][1]])
        else: print("Oops! Solution " + p[0][1] + " does not exist on the current map.")
    else: print("Oops! Invalid state for running solutions.")

def p_set_traverse(p): # dont really thing we need el traverse
    '''
    set_traverse : SET TRAVERSE TO INT INT COMMA INT INT
    '''
    if (built_map == False) and (built_sol == None):
        p[0] = ('TRAVERSE', p[4], p[5], p[7], p[8])
        c.setTraverse(p[4], p[5],p[7],p[8])
        print("Set traverse at", p[4], p[5],"and",p[7],p[8])
    else: print('Oops! "TRAVERSE" can only be invoked while creating a map.')

def p_go_down(p):
    '''
    go_down : MOVE DOWN
            | MOVE DOWN INT
            | MOVE DOWN LP INT RP
    '''
    if built_map and (built_sol== False):
        try:
            p[0] = ('DOWN', p[4])
        except:
            try:
                p[0] = ('DOWN', p[3])
            except:
                p[0] = ('DOWN', 1)
        if (current_map.add_move(current_solution, p[0])):
            c.moveDown(p[0])
            print(current_map.solutions[current_solution])
    else: print('Oops! "MOVE DOWN" can only be invoked while creating a solution.')

def p_exit_game(p): # NOTE THE RETURN...
    '''
    exit_game : EXIT
    '''
    p[0] = p[1]
    if(p[1] == 'exit') :
        print("See you later!")
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
        if (current_map.add_move(current_solution, p[0])):
            c.move_left(p[0])
            print(current_map.solutions[current_solution])
    else: print("Oops! Left can only be invoked while creating a solution.")

def p_undo_move(p): # NOTE THE RETURN...
    '''
    undo_move : UNDO
    '''
    if (built_map == True) and (built_sol == False):
        p[0] = 'UNDO'
        c.undoMove()
    else: print('Oops!! "UNDO" can only be invoked while creating a solution.')

def p_build_map(p): # MUST TAKE CARE... Build Map & Build Solution are the same...
    '''
    build_map : BUILD MAP ID
    '''
    global built_map
    if (built_map == False) and ( built_sol == None):
        p[0] = ('BUILD', p[3])
        built_map = True
    else: print('Oops! "BUILD MAP" can only be invoked while creating a map.')
    

def p_build_solution(p):
    '''
    build_solution : BUILD SOLUTION ID
    '''
    global  current_solution, built_sol, built_map
    p[0] = ('BUILD', p[2])
    if(built_map and built_sol == False):
        if(p[0][1] not in current_map.solutions):
            current_solution = None
            built_sol = True
            c.move_to_start()
        else: print("Oops! Solution " + p[0][1] + " already exists in " + current_map.place()) # verify..
    else: print("Oops! Solutions can be built while in solution creation mode.")
        

def p_go_right(p):
    '''
    go_right : MOVE RIGHT
            | MOVE RIGHT INT
            | MOVE RIGHT LP INT RP
    '''
    if built_map and (built_sol== False):
        try:
            p[0] = ('RIGHT', p[4])
        except:
            try:
                p[0] = ('RIGHT', p[3])
            except:
                p[0] = ('RIGHT', 1)
        if (current_map.add_move(current_solution, p[0])):
            c.moveRight(p[0])
            print(current_map.solutions[current_solution])
    else: print('Oops! "MOVE RIGHT" can only be invoked while creating a solution.')
    

def p_start_map(p):
    '''
    start_map : SET START AT INT INT
    '''
    if (built_map== False) and (built_sol == None):
        p[0] = ('START', p[4], p[5])
        c.setStart(p[4],p[5])
        print("Start map at ",p[4], p[5]) # testing
    else: print('Oops! "SET START" can only be invoked while creating a map.')

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
    global built_map
    global built_sol
    if not ((built_map and built_sol == False) or (built_sol == None and built_map == False)): # TODO -> VERIFY Boolean Predicate...
        c.create_map(p[0][1])
        built_map = False
        built_sol = None
        print("Creating " + p[0][1] + ".")
    else: print("Oops! Map can only be created while not in creation mode.")


def p_solution_assign(p):
    '''
    solution_assign : CREATE SOLUTION NAMED ID
    '''
    global built_sol
    if (built_map == True) and (built_sol==None):
        b = current_map.add_solution(p[4])
        print(p[4])
        if b : built_sol = False
        else : print("Oops! Solution " + p[4] + " already exists.")
    else: print('Oops! "CREATE SOLUTION" can only be invoked after a map is built.')


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
