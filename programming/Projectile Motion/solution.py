# https://physics.stackexchange.com/questions/580031/how-are-the-suvat-equations-derived

import math

def getdistance(height: float, velocity: float, angle: float) -> float:

    g = 9.81

    # velocity components
    vx = velocity * math.cos(angle)
    vy = velocity * math.sin(angle)

    # time of flight (positive root of quadratic)
    discriminant = vy**2 + 2 * g * height
    time = (vy + math.sqrt(discriminant)) / g

    # horizontal distance
    distance = vx * time

    return distance

while True:
    try:
        line = input()

        height, velocity, angle = map(float, line.split(','))

        distance = getdistance(height, velocity, angle)

        print(math.fabs(round(distance, 1))) # Round to nearest 10th

    except EOFError:
        break

