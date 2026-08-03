from environment.venue import Venue

from agents.crowd_generator import CrowdGenerator

from movement.movement import MovementEngine
from analyzer.density import DensityAnalyzer
from analyzer.flow import FlowAnalyzer
from scenarios.scenarios import ScenarioEngine
from analyzer.safety_score import SafetyScore
from analyzer.recommendation import RecommendationEngine



# Create Venue

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



# Generate Crowd

generator = CrowdGenerator()


crowd = generator.generate_crowd(
    number_of_people=600,
    entry_point=(10,0)
)



print(
    "Before Movement"
)


for person in crowd:

    print(
        person.person_id,
        person.get_position()
    )



# Movement Engine

movement = MovementEngine()



# Assign stage as destination

for person in crowd:

    movement.assign_target(
        person,
        (50,50)
    )



# Move crowd

movement.move_crowd(
    crowd
)



print("\nAfter Movement")


for person in crowd:

    print(
        person.person_id,
        person.get_position()
    )
# Crowd Density Analysis


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
# Crowd Flow Analysis


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
    average_speed,
    "m/s"
)



print(
    "Stopped Ratio:",
    stopped_ratio
)



print(
    "Movement Risk:",
    flow_risk
)   
# Scenario Simulation


scenario = ScenarioEngine(
    crowd,
    venue
)



# Test 1:
# Crowd increase


extra_people = scenario.increase_crowd(
    50
)


print(
    "\nScenario: Attendance +50%"
)


print(
    "Additional Visitors:",
    extra_people
)



# Test 2:
# Gate closure


gate_result = scenario.close_gate(
    "Gate A"
)


print(
    gate_result
)



# Test 3:
# Weather


weather_result = scenario.weather_change(
    "Heavy Rain"
)


print(
    weather_result
)

# Final Safety Evaluation


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



# Recommendations


recommendation = RecommendationEngine()


actions = recommendation.generate(
    risk,
    flow_risk
)



print("\nAI Recommendations:")


for action in actions:

    print("-", action)