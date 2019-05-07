import pyglet
from physicalobject import PhysicalObject

class Floor(PhysicalObject):

    def __init__(self, x, y):
        super(Floor, self).__init__(img=pyglet.resource.image("_white.png"), x=x, y=y, static=True)
        self.scale_x = 10
             