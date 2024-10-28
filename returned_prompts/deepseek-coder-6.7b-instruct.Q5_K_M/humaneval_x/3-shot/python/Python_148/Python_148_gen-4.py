    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    try:
        planet1_index = planets.index(planet1)
        planet2_index = planets.index(planet2)
    except ValueError:
        return ()

    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index

    return planets[planet1_index+1:planet2_index]


