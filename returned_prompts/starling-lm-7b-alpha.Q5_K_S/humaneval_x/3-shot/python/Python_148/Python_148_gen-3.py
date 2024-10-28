    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    elif planet1 == planet2:
        return (planet1,)
    elif planet1 > planet2:
        planet1, planet2 = planet2, planet1
    res = []
    for planet in planets:
        if planet > planet1 and planet < planet2:
            res.append(planet)
    return tuple(res)


