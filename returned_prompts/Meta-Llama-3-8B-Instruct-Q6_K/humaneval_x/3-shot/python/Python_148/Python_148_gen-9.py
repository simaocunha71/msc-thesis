    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet_index = {planet: i for i, planet in enumerate(planets)}

    if planet1 not in planet_index or planet2 not in planet_index:
        return ()

    start_index = planet_index[planet1]
    end_index = planet_index[planet2]

    return tuple(planets[i] for i in range(start_index + 1, end_index)) if start_index < end_index else ()
# or 
# return tuple(planets[i] for i in range(start_index + 1, end_index)) if start_index < end_index else tuple(planets[i] for i in range(end_index)) # for the case where planet1 is after planet2 in the solar system

    # for loop to sort the planets by proximity to the sun
    # sorted_planets = sorted(planets[i] for i in range(start_index + 1, end_index)) if start_index < end_index else sorted(planets[i:] for i in range(end_index))
    # return tuple(sorted_planets) if start_index < end_index else () 
    # return sorted_planets if start_index < end_index else ()  # for the case where planet1 is after planet2 in the solar system

    # another way to solve it
    # planets_between = [planet for planet in planets if start_index < planet_index[planet] < end_index]
    # return tuple(sorted(planets_between)) if start_index < end_index else ()  # for the case where planet1 is after planet2 in the solar system
    # return () if start_index > end_index else tuple(sorted(planets_between)) 
    # return tuple(sorted(planets_between))  # for the case where planet1 is after planet2 in the solar system
    # return ()  # for the case where planet1 is after planet2 in the solar system
    # return tuple(planets_between)  # for the case where planet1 is after planet2 in the solar system
    # return ()  # for the case where planet1 is after planet2 in the solar system
    # return tuple(sorted(planets_between))  # for the case where planet1 is after planet2 in the solar system
    # return tuple(planets_between)  # for the case where planet1 is after planet2 in the solar system
    #