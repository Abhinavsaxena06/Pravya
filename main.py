import pygame

from environment.venue import Venue
from environment.object import VenueObject

from agents.crowd_generator import CrowdGenerator

from movement.movement import MovementEngine

from analyzer.density import DensityAnalyzer
from analyzer.flow import FlowAnalyzer
from analyzer.safety_score import SafetyScore
from analyzer.recommendation import RecommendationEngine

from scenarios.scenarios import ScenarioEngine

from visualization.simulator import Simulator



# ==============================
# Create Venue
# ==============================

venue = Venue(
    100,
    100
)


venue.add_entry(
    10,
    0
)


venue.add_exit(
    90,
    100
)



# ==============================
# Create Infrastructure
# ==============================

stage = VenueObject(
    "Stage",
    50,
    50,
    10,
    10
)


medical = VenueObject(
    "Medical Station",
    20,
    70,
    8,
    8
)


food = VenueObject(
    "Food Court",
    70,
    40,
    15,
    10
)



venue.add_object(stage)
venue.add_object(medical)
venue.add_object(food)



# ==============================
# Generate Crowd
# ==============================

generator = CrowdGenerator()


crowd = generator.generate_crowd(
    number_of_people=200,
    entry_point=(10,0)
)



print("Before Movement")


for person in crowd:

    print(
        person.person_id,
        person.get_position()
    )



# ==============================
# Movement Engine
# ==============================

movement = MovementEngine()



for person in crowd:

    movement.assign_target(
        person,
        (50,50)
    )



movement.move_crowd(
    crowd
)



print("\nAfter Movement")


for person in crowd:

    print(
        person.person_id,
        person.get_position()
    )



# ==============================
# Density Analysis
# ==============================

density_analyzer = DensityAnalyzer()


density = density_analyzer.calculate_density(
    crowd,
    area=100
)


risk = density_analyzer.get_risk_level(
    density
)


print("\nCrowd Analysis")


print(
    "People:",
    len(crowd)
)


print(
    "Density:",
    density,
    "people/m²"
)


print(
    "Risk:",
    risk
)



# ==============================
# Flow Analysis
# ==============================

flow_analyzer = FlowAnalyzer()


average_speed = flow_analyzer.calculate_average_speed(
    crowd
)


stopped_ratio = flow_analyzer.stopped_people_ratio(
    crowd
)


flow_risk = flow_analyzer.movement_risk(
    average_speed,
    stopped_ratio
)



print("\nFlow Analysis")


print(
    "Average Speed:",
    average_speed
)


print(
    "Stopped Ratio:",
    stopped_ratio
)


print(
    "Movement Risk:",
    flow_risk
)



# ==============================
# Scenario Testing
# ==============================

scenario = ScenarioEngine(
    crowd,
    venue
)


extra_people = scenario.increase_crowd(
    50
)


print(
    "\nAdditional Visitors:",
    extra_people
)


print(
    scenario.close_gate("Gate A")
)


print(
    scenario.weather_change("Heavy Rain")
)



# ==============================
# Safety Evaluation
# ==============================

safety = SafetyScore()


final_score = safety.calculate(
    risk,
    flow_risk
)


status = safety.get_status(
    final_score
)



print("\n====================")

print("EVENT SAFETY REPORT")


print(
    "Safety Score:",
    final_score,
    "/100"
)


print(
    "Status:",
    status
)



# ==============================
# Recommendations
# ==============================

recommendation = RecommendationEngine()


actions = recommendation.generate(
    risk,
    flow_risk
)


print("\nAI Recommendations:")


for action in actions:

    print("-", action)



# ==============================
# Visualization
# ==============================

simulator = Simulator()



running = True



while running:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



    simulator.clear()



    # Draw infrastructure

    for obj in venue.objects:

        simulator.draw_object(
            obj
        )



    # Update movement

    movement.move_crowd(
        crowd
    )



    # Draw people

    for person in crowd:

        simulator.draw_person(
            person
        )



    simulator.update()


    simulator.clock.tick(60)



simulator.close()