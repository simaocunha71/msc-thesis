from math import floor
def wind_chill(temp, speed):
    temp = temp * 10 + speed
    speed = speed * speed
    return floor(-35.1 + 0.6 * temp - 0.4 * speed)