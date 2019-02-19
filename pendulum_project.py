import math

def update_system(acc, pos, vel, time1, time2):
    dt = time2 - time1
    newPos = initial_position * math.asin(math.sqrt(9.8/0.20)*dt
    newVel =