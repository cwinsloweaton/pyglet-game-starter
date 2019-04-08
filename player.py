import pyglet
from pyglet.window import key

class Player():

    def __init__(self, x, y):
        #Load spritesheet
        self.spritesheet = pyglet.resource.image("platformerPack_character.png")

        self.spritesheet_grid = pyglet.image.ImageGrid(self.spritesheet, 2, 4)
        #Assign the idle sprite as the players initial sprite
        self.sprite = pyglet.sprite.Sprite(self.spritesheet_grid[4], x=x, y=y)

        self.key_handler = key.KeyStateHandler()


    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.sprite.x -= 100 * dt
        if self.key_handler[key.RIGHT]:
            self.sprite.x += 100 * dt
        self.sprite.update()
    
    def draw(self):
        self.sprite.draw()