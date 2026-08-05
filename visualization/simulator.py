import pygame


class Simulator:

    def __init__(
            self,
            width=800,
            height=600
    ):

        pygame.init()

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode(
            (
                width,
                height
            )
        )

        pygame.display.set_caption(
            "Pravya AI - EventVerse Simulation"
        )

        self.clock = pygame.time.Clock()



    def clear(self):

        self.screen.fill(
            (20, 20, 20)
        )



    def draw_person(
            self,
            person
    ):

        # Convert simulation coordinates to screen coordinates
        scale = 5

        offset_x = 100
        offset_y = 50


        pygame.draw.circle(
            self.screen,

            # Person color
            (0, 255, 0),

            (
                int(person.x * scale + offset_x),
                int(person.y * scale + offset_y)
            ),

            5
        )



    def draw_object(
            self,
            obj
    ):

        scale = 5

        pygame.draw.rect(
            self.screen,

            # Object color
            (255, 255, 255),

            (
                int(obj.x * scale),
                int(obj.y * scale),
                int(obj.width * scale),
                int(obj.height * scale)
            )
        )



    def update(self):

        pygame.display.update()



    def close(self):

        pygame.quit()