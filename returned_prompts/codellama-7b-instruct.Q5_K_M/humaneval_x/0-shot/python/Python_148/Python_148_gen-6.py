
import math

# returns the distance between two planets
def distance(planet1, planet2):
    if planet1 == "Mercury":
        dist1 = 0
    elif planet1 == "Venus":
        dist1 = math.sqrt((6.71 * 10**8)**2 + (10.19 * 10**8)**2)
    elif planet1 == "Earth":
        dist1 = math.sqrt((6.37 * 10**6)**2 + (10.14 * 10**6)**2)
    elif planet1 == "Mars":
        dist1 = math.sqrt((6.39 * 10**6)**2 + (22.71 * 10**6)**2)
    elif planet1 == "Jupiter":
        dist1 = math.sqrt((7.14 * 10**7)**2 + (3.68 * 10**7)**2)
    elif planet1 == "Saturn":
        dist1 = math.sqrt((6.03 * 10**7)**2 + (4.38 * 10**7)**2)
    elif planet1 == "Uranus":
        dist1 = math.sqrt((4.07 * 10**7)**2 + (2.78 * 10**7)**2)
    elif planet1 == "Neptune":
        dist1 = math.sqrt((3.88 * 10**7)**2 + (2.47 * 10**7)**2)

    if planet2 == "Mercury":
        dist2 = 0
    elif planet2 == "Venus":
        dist2 = math.sqrt((6.71 * 10**8)**2 + (10.19 * 10**8)**2)
    elif planet2 == "Earth":
        dist2 = math.sqrt((6.37 * 10**6)**2 + (10.14 * 10**6)**2)
    elif planet2 == "M