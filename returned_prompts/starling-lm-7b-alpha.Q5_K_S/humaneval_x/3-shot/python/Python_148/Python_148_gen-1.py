    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    if planet1 > planet2:
        planet2, planet1 = planet1, planet2
    return tuple(planets[planets.index(planet1)+1:planets.index(planet2)])


