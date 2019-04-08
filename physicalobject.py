import pyglet

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0

    def update(self, dt):
        #gravity
        self.velocity_y += -9.8 * dt
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        

