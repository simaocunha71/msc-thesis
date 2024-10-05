    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        if planet1 == planet2:
            return (planet1,)
        elif planet1 == "Mercury" and planet2 != "Neptune":
            return tuple(planets[planets.index(planet1)+1:planets.index(planet2)])
        elif planet1 != "Mercury" and planet2 == "Neptune":
            return tuple(planets[planets.index(planet1)+1:])
        else:
            return tuple(planets[planets.index(planet1)+1:planets.index(planet2)])



