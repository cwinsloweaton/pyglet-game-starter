import pyglet
from player import Player
from floor import Floor

class Game(pyglet.window.Window):

    def __init__(self, width, height):
        super(Game, self).__init__(width=width, height=height)
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)

        self.player = Player(50, 300)
        self.floor = Floor(0, 10)

        self.push_handlers(self.player.key_handler)

        self.game_objects = [self.player, self.floor]

    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(1,0,0,1)
        for obj in self.game_objects:
            obj.draw()

    def update(self, dt):
        for obj in self.game_objects:
            if obj != self.player:
                if self.player.check_collision(obj):
                    self.player.y = obj.y + obj.height
                    self.player.velocity_y = 0
            obj.update(dt)
