    planet_names = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]

    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)

    if planet1_index == -1 or planet2_index == -1:
        return tuple()

    if planet1_index > planet2_index:
        return tuple(
            planet_names[planet1_index + 1 : planet2_index + 1]
            + planet_names[:planet1_index + 1]
        )

    return tuple(planet_names[planet1_index + 1 : planet2_index + 1])


