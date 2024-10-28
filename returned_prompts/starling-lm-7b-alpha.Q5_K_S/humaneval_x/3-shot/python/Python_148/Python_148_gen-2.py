    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    if planet1 == planet2:
        return (planet1,)
    if planet1 == "Mercury" and planet2 == "Neptune":
        return tuple(planets)
    if planet1 == "Mercury":
        return tuple(planets[:planets.index(planet2)+1])
    if planet2 == "Neptune":
        return tuple(planets[planets.index(planet1):])
    return tuple(planets[planets.index(planet1):planets.index(planet2)+1])


