import pyglet
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    """ Main method """
    pyglet.resource.path = ['images']
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    pyglet.app.run()

if __name__ == "__main__":
    main()