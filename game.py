import pyglet
from player import Player
from floor import Floor

class Game(pyglet.window.Window):

    def __init__(self, width, height):
        super(Game, self).__init__(width=width, height=height)
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)

        self.player = Player(50, 50)
        self.floor = Floor(0, 10)

        self.push_handlers(self.player.key_handler)

        self.game_objects = [self.player, self.floor]

    def on_draw(self):
        self.clear()
        for obj in self.game_objects:
            obj.draw()

    def update(self, dt):
        for obj in self.game_objects:
            obj.update(dt)
