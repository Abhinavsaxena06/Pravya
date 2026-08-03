class Venue:


    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.entries = []
        self.exits = []
        self.obstacles = []


    def add_entry(self, x, y):

        self.entries.append((x,y))


    def add_exit(self, x, y):

        self.exits.append((x,y))


    def add_obstacle(self, obstacle):

        self.obstacles.append(obstacle)


    def show_details(self):

        print("Venue Size:")
        print(
            self.width,
            "x",
            self.height
        )


        print("Entries:", self.entries)

        print("Exits:", self.exits)