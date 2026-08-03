import math



class FlowAnalyzer:


    def calculate_average_speed(
            self,
            people
    ):


        if len(people) == 0:
            return 0


        total_speed = 0


        for person in people:

            total_speed += person.current_speed


        average = total_speed / len(people)


        return round(
            average,
            2
        )



    def stopped_people_ratio(
            self,
            people,
            speed_threshold=0.5
    ):


        if len(people)==0:
            return 0


        stopped = 0


        for person in people:

            if person.current_speed < speed_threshold:

                stopped += 1



        ratio = stopped / len(people)


        return round(
            ratio,
            2
        )



    def movement_risk(
            self,
            average_speed,
            stopped_ratio
    ):


        risk_score = 0



        # Low movement speed
        if average_speed < 1:

            risk_score += 40



        # Too many stopped people
        if stopped_ratio > 0.3:

            risk_score += 40



        if risk_score >=70:

            return "HIGH"



        elif risk_score >=40:

            return "MEDIUM"



        else:

            return "LOW"