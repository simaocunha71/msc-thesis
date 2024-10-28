    planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    if planet1 not in planet_list or planet2 not in planet_list:
        return ()

    if planet1 == planet2:
        return (planet1,)

    if planet1 == "Mercury":
        return tuple(planet_list[planet_list.index(planet1) + 1:planet_list.index(planet2)])
    else:
        return tuple(planet_list[planet_list.index(planet1) + 1:planet_list.index(planet2)])


