# Hunter inherits from the Pulsator (1st) and the Mobile_Simulton (2nd) class:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    constant = 200
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0, 5)


    def update(self,model):
        eaten = Pulsator.update(self,model)
        self.move()

        nearst = list(model.find(self.locate))
        if len(nearst) > 1:

            nearst = min([(i.distance(self.get_location()), i) for i in nearst  ])[1]
        elif len(nearst) == 1: nearst = nearst[0]


        if type(nearst) != list:
            center_h = self.get_location()
            center_ball = nearst.get_location()

            y, x = center_ball[1] - center_h[1],  center_ball[0] - center_h[0]
            angle = atan2(y,x)
            self.set_angle(angle)
        return eaten



    def locate(self,ball):

        return isinstance(ball,Prey) and  ball.distance(self.get_location()) <= self.constant

