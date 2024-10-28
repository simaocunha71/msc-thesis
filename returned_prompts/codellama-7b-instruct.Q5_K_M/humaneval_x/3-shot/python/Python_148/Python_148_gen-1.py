    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)

    return tuple(
        sorted(
            planets[planet1_index:planet2_index + 1], 
            key=lambda planet: (planets.index(planet), planet)
        )
    )


