import pyglet
from pyglet.window import key
from projectile import Projectile
from physicalobject import PhysicalObject
from floor import Floor

class Player(PhysicalObject):

    def __init__(self, x, y):
        #Load spritesheet
        self.spritesheet = pyglet.resource.image("platformerPack_character.png")
        self.spritesheet_grid = pyglet.image.ImageGrid(self.spritesheet, 2, 4)
        super().__init__(img=self.spritesheet_grid[4], x=x, y=y)

        self.key_handler = key.KeyStateHandler()
        self.move_force = 50
        self.grounded = False

        self.projectiles = []


    def draw(self):
        super().draw()
        for projectile in self.projectiles:
            projectile.draw()

    def update(self, dt):
        if self.key_handler[key.RSHIFT]:
            self.velocity_y -= self.move_force
        if self.key_handler[key.LEFT]:
            self.velocity_x = -self.move_force
        if self.key_handler[key.RIGHT]:
            self.velocity_x = self.move_force
        if self.key_handler[key.SPACE]:
            if self.grounded:
                self.jump(200)
                self.grounded = False
        if self.key_handler[key.F]:
           self.fire()
        super().update(dt)

        self.velocity_x = 0

        for projectile in self.projectiles:
            projectile.update(dt)

    def jump(self, power):
        self.velocity_y = power
    
    def fire(self):
        self.projectiles.append(Projectile(self.x, self.y, 100, 0))

    def check_collision(self, other):
        if isinstance(super().check_collision(other), Floor):
            self.grounded = True
