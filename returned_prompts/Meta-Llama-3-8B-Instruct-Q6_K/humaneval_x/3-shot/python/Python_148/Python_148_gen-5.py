    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet_dict = {planet: i for i, planet in enumerate(planets)}

    if planet1 not in planets or planet2 not in planets:
        return ()

    planet1_index = planet_dict[planet1]
    planet2_index = planet_dict[planet2]

    result = []
    for i in range(min(planet1_index, planet2_index) + 1, max(planet1_index, planet2_index)):
        result.append(planets[i])

    return tuple(result)  # Convert list to tuple


