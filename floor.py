import pyglet

class Floor(pyglet.sprite.Sprite):

    def __init__(self, x, y):
        super(Floor, self).__init__(img=pyglet.resource.image("_white.png"), x=x, y=y)
        self.scale_x = 10
        
"https://github.com/cwinsloweaton/pyglet-game-starter"



""" if(player1.x < player2.x + player2.width &&
    player1.x + player1.width > player2.x &&
    player1.y < player2.y + player2.height &&
    player1.y + player1.height > player2.y)
{
    System.out.println("Collision Detected");
} """
        