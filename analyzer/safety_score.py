class SafetyScore:


    def __init__(self):

        self.score = 100



    def calculate(
            self,
            density_risk,
            flow_risk
    ):


        score = 100



        # Density impact

        if density_risk == "HIGH":

            score -= 40


        elif density_risk == "MEDIUM":

            score -= 20



        # Flow impact

        if flow_risk == "HIGH":

            score -= 40


        elif flow_risk == "MEDIUM":

            score -= 20



        if score < 0:

            score = 0



        return score



    def get_status(
            self,
            score
    ):


        if score >= 80:

            return "SAFE"


        elif score >= 50:

            return "MODERATE"


        else:

            return "DANGEROUS"