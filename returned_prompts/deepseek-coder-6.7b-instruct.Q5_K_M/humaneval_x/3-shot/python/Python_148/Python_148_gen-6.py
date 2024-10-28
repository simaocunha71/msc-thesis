    planets_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if planet1 not in planets_order or planet2 not in planets_order:
        return ()

    planet1_index = planets_order.index(planet1)
    planet2_index = planets_order.index(planet2)

    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index

    return tuple(planets_order[planet1_index+1:planet2_index])


