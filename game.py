import pyglet
from player import Player

class Game(pyglet.window.Window):

    def __init__(self, width, height):
        super(Game, self).__init__(width=width, height=height)
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)

        self.label = pyglet.text.Label('This is a label!', x=10, y=10)

        self.player = Player(50, 50)

        self.push_handlers(self.player.key_handler)

    def on_draw(self):
        self.clear()
        self.label.draw()
        self.player.draw()

    def update(self, dt):
        self.player.update(dt)
