
def bf(planet1, planet2):
    # planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index == -1 or planet2_index == -1:
        return ()
    return tuple(planet_names[planet1_index + 1:planet2_index + 1])
