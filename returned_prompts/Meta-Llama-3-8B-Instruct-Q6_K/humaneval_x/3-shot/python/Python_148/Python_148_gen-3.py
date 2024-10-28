    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet_index1 = planets.index(planet1)
    planet_index2 = planets.index(planet2)

    if planet_index1 < 0 or planet_index2 < 0:
        return ()

    planets_between = planets[planet_index1 + 1:planet_index2]
    return tuple(planets_between) if planets_between else ()  # if planets_between is empty, return empty tuple


