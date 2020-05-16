import math

def getAngle(OGx, OGy, robotx, roboty):
    x = OGx - robotx
    y = OGy - roboty
    if x == 0:
        if y > 0:
            return 0;
        else:
            return math.pi * -1

    angle = math.atan2(y, x)
    return angle - (math.pi/2)

robotx = 34
roboty =