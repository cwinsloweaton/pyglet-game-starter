import pyglet
from physicalobject import PhysicalObject

class Projectile(PhysicalObject):

    def __init__(self, x, y, velocity_x, velocity_y):
        super(Projectile, self).__init__(img=pyglet.resource.image("boomerang.png"), x=x, y=y)
        self.scale = 0.3
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def draw(self):
        super().draw()
