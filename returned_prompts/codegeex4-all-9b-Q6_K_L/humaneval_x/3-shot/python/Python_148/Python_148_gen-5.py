    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1_index = planets.index(planet1)
    p2_index = planets.index(planet2)

    if p1_index == -1 or p2_index == -1:
        return ()

    if p1_index > p2_index:
        return tuple(planets[p1_index + 1:p2_index])
    else:
        return tuple(planets[p2_index + 1:p1_index])

