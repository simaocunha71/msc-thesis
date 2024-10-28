
def bf(planet1, planet2):
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    i1 = planets.index(planet1)
    i2 = planets.index(planet2)
    if i1 == -1 or i2 == -1: return ()
    return tuple(planets[i:i+1] for i in range(min(i1, i2), max(i1, i2)+1))
