    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    try:
        start = planets.index(planet1)
        end = planets.index(planet2)
    except ValueError:
        return ()

    if start < end:
        return tuple(planets[start + 1:end])
    else:
        return tuple(planets[end + 1:start])