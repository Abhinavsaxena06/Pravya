class Venue:


    def __init__(
            self,
            width,
            height
    ):

        self.width = width
        self.height = height

        self.entries = []
        self.exits = []

        self.objects = []



    def add_entry(
            self,
            x,
            y
    ):

        self.entries.append(
            (x,y)
        )



    def add_exit(
            self,
            x,
            y
    ):

        self.exits.append(
            (x,y)
        )



    def add_object(
            self,
            obj
    ):

        self.objects.append(obj)