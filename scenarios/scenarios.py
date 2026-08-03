class ScenarioEngine:


    def __init__(self, crowd, venue):

        self.crowd = crowd
        self.venue = venue



    def increase_crowd(
            self,
            percentage
    ):

        current_people = len(self.crowd)


        additional_people = int(
            current_people * percentage / 100
        )


        return additional_people



    def close_gate(
            self,
            gate_name
    ):

        print(
            gate_name,
            "is now closed"
        )


        return {
            "event": "gate_closed",
            "gate": gate_name
        }



    def weather_change(
            self,
            condition
    ):

        return {
            "event": "weather_change",
            "condition": condition
        }



    def medical_emergency(
            self,
            location
    ):

        return {
            "event": "medical_emergency",
            "location": location
        }