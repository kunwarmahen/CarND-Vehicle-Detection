class Vehicle:
    def __init__(self):
        self.minx = None
        self.miny = None
        self.maxx = None
        self.maxy = None
        self.avgx = None
        self.avgy = None
    
    def setValues(self, minx, miny, maxx, maxy):
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxx
        self.calculateAvg()
    
    def calculateAvg(self):
        self.avgx = self.maxx - self.minx
        self.avgy = self.maxy - self.miny
        