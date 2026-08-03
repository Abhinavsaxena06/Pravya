class Person:

    def __init__(self, person_id, x, y, speed, behavior):

        # Unique person ID
        self.person_id = person_id

        # Current position
        self.x = x
        self.y = y

        # Speed parameters
        self.base_speed = speed
        self.current_speed = speed

        # Crowd behavior type
        self.behavior = behavior

        # Set speed according to behavior
        self.update_behavior_speed()


    def move(self, target_x, target_y):

        # Direction vector
        dx = target_x - self.x
        dy = target_y - self.y

        # Distance from target
        distance = (dx ** 2 + dy ** 2) ** 0.5


        # Move only if target is not reached
        if distance > 0:

            self.x += (dx / distance) * self.current_speed
            self.y += (dy / distance) * self.current_speed



    def get_position(self):

        return (self.x, self.y)



    def update_behavior_speed(self):

        if self.behavior == "elderly":

            self.current_speed = self.base_speed * 0.6


        elif self.behavior == "family":

            self.current_speed = self.base_speed * 0.8


        elif self.behavior == "excited":

            self.current_speed = self.base_speed * 1.3


        elif self.behavior == "panic":

            self.current_speed = self.base_speed * 1.5


        else:

            self.current_speed = self.base_speed