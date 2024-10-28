    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    try:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
    except ValueError:
        return ()

    if idx1 > idx2:
        idx1, idx2 = idx2, idx1

    return tuple(planets[idx1 + 1:idx2])

