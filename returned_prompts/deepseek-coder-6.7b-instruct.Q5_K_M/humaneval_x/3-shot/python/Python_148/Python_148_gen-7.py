    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        idx1, idx2 = planets.index(planet1), planets.index(planet2)
        return tuple(planets[idx1+1:idx2])
    except ValueError:
        return ()


