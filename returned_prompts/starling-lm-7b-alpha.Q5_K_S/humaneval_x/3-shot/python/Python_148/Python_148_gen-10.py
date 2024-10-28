    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()

    result = []
    if planet1 == planet2:
        return result

    for i in range(len(planets)):
        if planets[i] == planet1:
            left = i
        elif planets[i] == planet2:
            right = i

    for i in range(left, right + 1):
        result.append(planets[i])

    return tuple(result)


