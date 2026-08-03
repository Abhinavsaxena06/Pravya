import math



class MovementEngine:


    def __init__(self):

        self.targets = {}



    def assign_target(
            self,
            person,
            target
    ):

        self.targets[person.person_id] = target



    def move_person(
            self,
            person
    ):


        if person.person_id not in self.targets:
            return


        target = self.targets[
            person.person_id
        ]


        person.move(
            target[0],
            target[1]
        )



    def move_crowd(
            self,
            crowd
    ):

        for person in crowd:

            self.move_person(person)