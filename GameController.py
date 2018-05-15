import AppGUI as g

class Controller():
    def __init__(self):
        self.app = g.App()
        self.app.init_display()
    
    def moveDown(self,steps):
        self.app.operate(steps)

    def moveRight(self, steps):
        self.app.operate(steps)

    def setStart(self, x, y):
        self.app.set_start(x, y)

    def setEnd(self, x,y):
        self.app.set_end(x,y)

    #  will nort be implemented
    # def setTraverse(self, startX, startY, endX, endY):
    #     self.setStart(startX,startY)
    #     self.setEnd(endX,endY)
    #
    # def undoMove(self):
    #     pass


    def run_solution(self, moves):
        self.app.run_solution(moves)

    def create_map(self, name):
        pass

    def move_up(self, moves):
        self.app.operate(moves)

    def set_end(self, x,y):
        self.app.set_end(x, y)

    def move_left(self, moves):
        self.app.operate(moves)

    def switch_map(self, map):
        pass

    def add_obstacle(self, map, obj, x, y):
        self.app.add_object(x, y)

    def move_to_start(self):
        self.app.move_to_start()
    
