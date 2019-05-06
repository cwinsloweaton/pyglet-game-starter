import pyglet

class Floor(pyglet.sprite.Sprite):

    def __init__(self, x, y):
        super(Floor, self).__init__(img=pyglet.resource.image("_white.png"), x=x, y=y)
        self.scale_x = 10
             