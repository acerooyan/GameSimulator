# Black_Hole inherits from only Simulton, updating by finding/removing
#   any Prey-derived class whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10

    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)


        self.color = 'black'
    def update(self,model):

        eat_balls = [i for i in model.find(self.contains) if isinstance(i,Prey)]

        model.remove(eat_balls)
        return eat_balls
    def contains(self,ball):
        if type(ball) == tuple:
            if self.distance(ball) < Black_Hole.radius:
                return  [ball]
        else:
            return  self.distance(ball.get_location()) < Black_Hole.radius




    def display(self, canvas):
        self.dimension = self.get_dimension()[0] / 2
        canvas.create_oval(self._x - self.dimension  , self._y - self.dimension ,
                           self._x + self.dimension , self._y + self.dimension ,
                           fill=self.color)


