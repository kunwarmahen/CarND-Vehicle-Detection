class Frame:
    def __init__(self):
        self.detected = False
        self.no = 0
        self.vehicle = list()
    
    def toString(self):
        print('Frame No:', self.no)
        print('Detected', self.detected)
        for vehicle in self.vehicle:
            print('Vehicle Minx', vehicle.minx)
            print('Vehicle Miny', vehicle.miny)
            print('Vehicle Maxx', vehicle.maxx)
            print('Vehicle Maxy', vehicle.maxy)
            print('--------------------')
        print('================')