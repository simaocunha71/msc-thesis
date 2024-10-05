
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    elif planet1 == planet2:
        return (planet1,)
    elif planet1 > planet2:
        planet1, planet2 = planet2, planet1
    res = []
    for p in planets:
        if p > planet1 and p < planet2:
            res.append(p)
    return tuple(res)

# Alternative Solution
def bf2(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    elif planet1 == planet2:
        return (planet1,)
    elif planet1 > planet2:
        planet1, planet2 = planet2, planet1
    res = []
    for p in planets:
        if p > planet1 and p < planet2:
            res.append(p)
    return tuple(res)

# Testing
print(bf("Jupiter", "Neptune") == ("Saturn", "Uranus"))
print(bf("Earth", "Mercury") == ("Venus"))
print(bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
print(bf2("Jupiter", "Neptune") == ("Saturn", "Uranus"))
print(bf2("Earth", "Mercury") == ("Venus"))
print(bf2("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

# Alternative Testing
test = ["Jupiter", "Saturn", "Uranus", "Neptune", "Mercury", "Venus", "