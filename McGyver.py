

class McGyver:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lstObj = [False, False, False]
    def move(self,x,y):
        self.x += x
        self.y += y
        
