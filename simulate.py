from model import SimpleRoboticsAI
import random

ai = SimpleRoboticsAI()

for step in range(10):
    sensor_data = {
        "obstacle": random.choice([True, False]),
        "battery": random.randint(10, 100)
    }
    action = ai.decide(sensor_data)
    print(f"Step {step}: sensors={sensor_data} → action={action}")
