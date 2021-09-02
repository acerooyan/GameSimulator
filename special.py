#special has method inherited from Hunter and Mobile_simulation

# It has longer time to shrink -> 200 cycles, and it has yellow color at first
# when special eats a ball object it grows and change the color to yellow, when it eats floater it shrinks and change the color to purple

from hunter import Hunter
from mobilesimulton import Mobile_Simulton
from ball import Ball


class Special(Hunter, Mobile_Simulton):
    counter_constant = 200

    def __init__(self, x, y):
        Hunter.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0, 5)
        self.color = 'yellow'
    def update(self, model):
        eaten = Hunter.update(self, model)

        for i in eaten:
            if isinstance(i,Ball):
                self.change_dimension(1, 1)
                self.color = 'yellow'
            else:
                self.change_dimension(-2, -2)
                self.color = 'purple'
