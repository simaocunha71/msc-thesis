    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planets and planet2 in planets:
        planet_list = []
        planet_index1 = planets.index(planet1)
        planet_index2 = planets.index(planet2)
        for i in range(planet_index1, planet_index2):
            planet_list.append(planets[i])
        for i in range(planet_index2, planet_index1):
            planet_list.append(planets[i])
        return tuple(planet_list)
    else:
        return ()


