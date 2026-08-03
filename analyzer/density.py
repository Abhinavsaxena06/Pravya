class DensityAnalyzer:


    def __init__(self, danger_threshold=5):

        # people per square meter
        self.danger_threshold = danger_threshold



    def calculate_density(
            self,
            people,
            area
    ):

        if area <= 0:
            return 0


        density = len(people) / area


        return round(
            density,
            2
        )



    def get_risk_level(
            self,
            density
    ):


        if density < 2:

            return "LOW"


        elif density < self.danger_threshold:

            return "MEDIUM"


        else:

            return "HIGH"