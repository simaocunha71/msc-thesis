
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    start = planets.index(planet1)
    end = planets.index(planet2)
    return tuple(planets[i] for i in range(start, end + 1))


# Alternative solution:

def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    return tuple(sorted(planets[planets.index(planet1):planets.index(planet2)+1]))


# Or:

def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    return tuple(planets[planets.index(planet1):planets.index(planet2)+1])


# Or:

def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    i, j = planets.index(planet1), planets.index(planet2)
    return tuple(planets[k] for k in range(i, j + 1))


# Or:

def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Ne