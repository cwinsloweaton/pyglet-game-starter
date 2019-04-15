import pyglet
from pyglet.window import key
from physicalobject import PhysicalObject

class Player(PhysicalObject):

    def __init__(self, x, y):
        #Load spritesheet
        self.spritesheet = pyglet.resource.image("platformerPack_character.png")
        self.spritesheet_grid = pyglet.image.ImageGrid(self.spritesheet, 2, 4)
        super().__init__(img=self.spritesheet_grid[4], x=x, y=y)

        self.key_handler = key.KeyStateHandler()

        self.move_force = 50
        self.grounded = False

    def on_draw(self):
        super().on_draw()

    def update(self, dt):
        

        if self.key_handler[key.LEFT]:
            self.velocity_x = -self.move_force
        if self.key_handler[key.RIGHT]:
            self.velocity_x = self.move_force
        super().update(dt)

        self.velocity_x = 0