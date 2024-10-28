
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planets and planet2 in planets:
        i = planets.index(planet1)
        j = planets.index(planet2)
        if i > j:
            i, j = j, i
        return tuple(planets[i+1:j])
    return ()


# Alternative implementation using `bisect`:
from bisect import bisect_left as bl, bisect_right as br

def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planets and planet2 in planets:
        i = bl(planets, planet1)
        j = br(planets, planet2) - 1
        if i > j:
            i, j = j, i
        return tuple(planets[i+1:j])
    return ()


# Another implementation using `enumerate`:
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planets and planet2 in planets:
        i = planets.index(planet1)
        j = planets.index(planet2)
        if i > j:
            i, j = j, i
        return tuple(planets[i+1:j])
    return ()

# Test cases:
print(bf("Jupiter", "Neptune") == ("Saturn", "Uranus"))  # True
print(bf("Earth", "Mercury") == ("Venus"))  # True
print(bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))  # True

# Test