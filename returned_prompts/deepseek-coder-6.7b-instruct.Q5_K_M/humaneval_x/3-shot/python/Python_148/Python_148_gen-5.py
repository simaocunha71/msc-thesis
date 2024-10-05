    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    planet1_index = planets.index(planet1) if planet1 in planets else -1
    planet2_index = planets.index(planet2) if planet2 in planets else -1

    if planet1_index == -1 or planet2_index == -1:
        return ()

    return planets[planet1_index+1:planet2_index]


