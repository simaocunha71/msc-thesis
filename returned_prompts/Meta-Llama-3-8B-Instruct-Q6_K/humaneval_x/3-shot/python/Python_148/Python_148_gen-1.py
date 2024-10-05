    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet_index1 = planets.index(planet1)
    planet_index2 = planets.index(planet2)

    if planet_index1 == -1 or planet_index2 == -1:
        return ()

    result = planets[planet_index1+1:planet_index2]
    result.sort(key=lambda x: planets.index(x))
    return tuple(result)  # Convert the list to a tuple


