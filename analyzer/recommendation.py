class RecommendationEngine:



    def generate(
            self,
            density_risk,
            flow_risk
    ):


        recommendations = []



        if density_risk == "HIGH":

            recommendations.append(
                "Open additional entry or exit points"
            )



        if flow_risk == "HIGH":

            recommendations.append(
                "Redirect crowd movement"
            )



        if len(recommendations)==0:

            recommendations.append(
                "Continue monitoring"
            )



        return recommendations