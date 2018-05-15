
class Grid: # city...

    def __init__(self, place):
        self.place = place
        self.objects = {}
        self.person = None
        self.solutions = {}

    def add_solution(self, key):
        if(key not in self.solutions):
            self.solutions[key] = []
            return True
        else: return False

    def add_move(self, key, move):
        if(key in self.solutions):
            self.solutions[key].append(move)
            return True
        else: return False

    def open_grid(self): # pygame...
        pass

    def close_grid(self): # pygame...
        pass

    def refresh_grid(self): # pygame...
        pass

    def add_object(self, x, y, thing):
        if (x, y) in self.objects : print ("Oops! There is already an object here.")
        else : self.objects[(x, y)] = Object(x, y, thing)

    def remove_object(self, x, y):
        if (x, y) in self.objects :
            self.objects[(x, y)] = None
            del self.objects[(x, y)]
            print("The object has been removed.")
        else : print("Oops! There is no object there.")

    def move_object(self, x1, y1, x2, y2):
        if (x1, y1) in self.objects:
            if (x2, y2) not in self.objects:
                self.objects[(x2, y2)] = self.objects[(x1, y1)]
                self.objects[(x1, y1)] = None
                del self.objects[(x1, y1)]
                print("The object has been moved.")
            else : print("Oops! It is not possible to move the object to that position.")
        else : print("Oops! There is no object there.")

    def validate_traverse(self, traverse): # pygame...
        pass

class Object:

    def __init__(self, x, y, thing):
        self.x = x
        self.y = y
        self.thing = thing # type...

class Player(Object):

    def __init__(self, x, y):
        super().__init__(x, y, "PLAYER") # TODO -> det. how are we going to accept the player-type param.
        # current player position... (will change during traverse...)
        self.current_x = x
        self.current_y = y

    def move_to_start(self): # move to initial position...
        self.current_x = self.x
        self.current_y = self.y

class Traverse:

    def __init__(self, name):
        self.name = name
        self.moves = []

    def __len__(self) : return len(self.moves)

    def add_move(self, move): # add_last...
        self.moves.insert(len(self.moves), move)

    def delete_prev_move(self, move): # delete_last... (UNDO)
        self.moves.pop()

    def is_empty(self) : return len(self) == 0

    def traverse(self) : return self.moves