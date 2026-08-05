class VenueObject:


    def __init__(
            self,
            name,
            x,
            y,
            width,
            height
    ):

        self.name = name

        self.x = x
        self.y = y

        self.width = width
        self.height = height



    def get_position(self):

        return (
            self.x,
            self.y
        )