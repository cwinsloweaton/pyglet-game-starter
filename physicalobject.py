import pyglet


class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0

    def get_bottom(self):
        return self.y + self.height

    def get_right(self):
        return self.x + self.width

    def update(self, dt):
        # gravity
        self.velocity_y += - 80 * dt
        
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def check_collision(self, other):
        """ if (self.x < other.x + other.width
            and self.x + other.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y):
            #print("collision")
            return True
        return False """

        b_collision = other.get_bottom() - self.y
        t_collision = self.get_bottom() - other.y
        l_collision = self.get_right() - other.x
        r_collision = other.get_right() - self.x

        if t_collision < b_collision and t_collision < l_collision and t_collision < r_collision:
            #top collision
        if b_collision < t_collision and b_collision < l_collision and b_collision < r_collision:
            #bottom collision
        if l_collision < r_collision and l_collision < t_collision and l_collision < b_collision:
            #left collision
        if r_collision < l_collision and r_collision < t_collision and r_collision < b_collision:
            #right collision
