import random

class SimpleRoboticsAI:
    """
    Minimal Robotics AI agent for testnet simulation.
    """

    def decide(self, sensor_data):
        if sensor_data.get("obstacle"):
            return "turn_left"
        if sensor_data.get("battery", 100) < 20:
            return "charge"
        return random.choice(["move_forward", "scan", "idle"])
