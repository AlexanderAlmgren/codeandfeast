import math

gravity = 9.81

def getdistance(height: float, velocity: float, angle: float) -> float:

    # PUT YOUR CODE HERE

while True:
    try:
        line = input()

        height, velocity, angle = map(float, line.split(','))

        distance = getdistance(height, velocity, angle)

        print(math.fabs(round(distance, 1)))

    except EOFError:
        break

