import random

from agents.person import Person
from agents.behaviour import BEHAVIORS



class CrowdGenerator:


    def __init__(self):

        self.people = []


    def generate_crowd(
            self,
            number_of_people,
            entry_point
    ):


        behavior_types = list(BEHAVIORS.keys())


        for i in range(number_of_people):

            behavior = random.choice(
                behavior_types
            )


            speed = BEHAVIORS[behavior]["speed"]


            person = Person(
                person_id=i,
                x=entry_point[0],
                y=entry_point[1],
                speed=speed,
                behavior=behavior
            )


            self.people.append(person)


        return self.people



    def get_crowd_size(self):

        return len(self.people)