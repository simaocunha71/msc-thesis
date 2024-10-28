    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    result = []

    if planet1 not in planets or planet2 not in planets:
        return result
    if planet1 == planet2:
        return result

    for i in range(planets.index(planet1), planets.index(planet2)+1):
        result.append(planets[i])

    return result


