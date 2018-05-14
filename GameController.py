class Controller():

    def exit(self):
        pass
    
    def moveDown(self,steps):
        pass

    def moveRight(self, steps):
        pass

    def setStart(self, x, y):
        pass

    def setEnd(self, x,y):
        pass
    
    def setTraverse(self, startX, startY, endX, endY):
        self.setStart(startX,startY)
        self.setEnd(endX,endY)

    def undoMove(self):
        pass

    def buildMap(self, name): #this name should be set as label for pygame window.
        pass

    def createSolution(self, name):
        pass

    
    
