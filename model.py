import controller
import model   # Use to pass a reference to this module when calling update in update_all

#Use the reference to this module to pass it to update methods

from ball      import Ball
#from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import  Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
balls       = set()
select = None
step = False

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, balls
    running = False
    cycle_count = 0
    balls = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global step, running

    step = True
    running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)
def select_object(kind):
    global select

    select = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):

    if select == 'Remove':
        def contains(s):
            return s.contains((x, y))
        remove(find(contains))

    elif select != None:
        balls.add( eval(select + '(x,y)'))



#add simulton s to the simulation
def add(s):
    pass


# remove simulton s from the simulation
def remove(s):
    global balls
    for i in s:
        balls.remove(i)
#find/return a set of simultons that each satisfy predicate p
def find(p):
    return {i for i in balls if p(i)}


#call update for every simulton (passing model to each) in the simulation
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count,running, step
    if running:
        cycle_count += 1
        for b in list(balls):
            b.update(model)
    elif step == True:
        cycle_count += 1
        running = True
        for b in list(balls):
            b.update(model)
        step = False
        running = True

#For animation: (1) delete every simulton from the canvas; (2) call display on
#  each simulton being simulated to add it back to the canvas, possibly in a
#  new location; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)

    for b in balls:
        b.display(controller.the_canvas)

    controller.the_progress.config(text=  str(cycle_count) + " cycles/" + str(len(balls)) + " simultons")
