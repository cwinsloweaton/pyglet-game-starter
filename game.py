import pyglet
from player import Player
from enemy import Enemy
from floor import Floor
from physicalobject import PhysicalObject

class Game(pyglet.window.Window):

    def __init__(self, width, height):
        super(Game, self).__init__(width=width, height=height)
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)
        self.fps_display = pyglet.clock.ClockDisplay()
        self.player = Player(50, 300)
        self.floor = Floor(0, 10)
        self.enemy = Enemy(300, 400)
        self.push_handlers(self.player.key_handler)

        self.game_objects = [self.player, self.floor, self.enemy]

    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(1,0,0,1)
        for obj in self.game_objects:
            obj.draw()
        self.fps_display.draw()

    def update(self, dt):
        for obj in self.game_objects:
            for other_obj in self.game_objects:
                if other_obj == obj or not isinstance(obj, PhysicalObject):
                    continue
                    
                obj.check_collision(other_obj)
            obj.update(dt)
