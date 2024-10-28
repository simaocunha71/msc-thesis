    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if planet1 not in planet_names or planet2 not in planet_names:
        return ()

    idx1 = planet_names.index(planet1)
    idx2 = planet_names.index(planet2)

    result = tuple(planets[idx1+1:idx2])

    return result


