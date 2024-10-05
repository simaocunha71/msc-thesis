
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        if planet1 == planet2:
            return (planet1,)
        elif planet1 == "Mercury":
            return (planet1, planet2)
        elif planet2 == "Neptune":
            return tuple(planet for planet in planets[:-1] if planet != planet1 and planet != planet2)
        else:
            index_planet1 = planets.index(planet1)
            index_planet2 = planets.index(planet2)
            return tuple(planet for index, planet in enumerate(planets[index_planet1+1:index_planet2]) if planet != planet1 and planet != planet2)



