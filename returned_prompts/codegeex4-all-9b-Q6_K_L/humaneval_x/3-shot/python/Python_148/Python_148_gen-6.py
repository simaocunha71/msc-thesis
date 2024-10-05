    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)

    if idx1 == -1 or idx2 == -1:
        return ()

    if idx1 > idx2:
        idx1, idx2 = idx2, idx1

    return tuple(planets[idx1 + 1:idx2])


