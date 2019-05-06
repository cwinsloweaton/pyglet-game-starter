import pyglet
from physicalobject import PhysicalObject

class Enemy(PhysicalObject):

    def __init__(self, x, y):
        super().__init__(img=pyglet.resource.image("_white.png"), x=x, y=y)
