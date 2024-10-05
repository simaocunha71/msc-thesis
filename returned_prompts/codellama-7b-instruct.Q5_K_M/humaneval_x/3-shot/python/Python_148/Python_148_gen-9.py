    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()

    i = planets.index(planet1)
    j = planets.index(planet2)

    if i > j:
        return tuple(planets[i:j+1])
    else:
        return tuple(planets[j:i+1])


