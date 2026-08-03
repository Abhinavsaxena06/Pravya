class ScenarioRiskAnalyzer:


    def analyze_gate_failure(
            self,
            current_density
    ):


        new_density = current_density * 1.5



        if new_density > 5:

            risk = "HIGH"


        elif new_density > 3:

            risk = "MEDIUM"


        else:

            risk = "LOW"



        return {

            "new_density":
            round(new_density,2),

            "risk":
            risk
        }