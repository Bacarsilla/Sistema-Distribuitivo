class Somar:
    def __init__(self, x:float, y:float):
        self.x = 0
        self.y = 0
        self.res = 0


    def executar(self, x, y)->float:
        self.x = x
        self.y = y
        self.res = self.x + self.y
        return self.res