    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet_index1 = planets.index(planet1)
    planet_index2 = planets.index(planet2)

    if planet_index1 < 0 or planet_index2 < 0:
        return ()

    planets_between = planets[planet_index1 + 1:planet_index2]
    return tuple(sorted(planets_between)) if planets_between else ()
# test cases
print(bf("Jupiter", "Neptune"))  # ==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  # ==> ("Venus")
print(bf("Mercury", "Uranus"))  # ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Pluto", "Uranus"))  # ==> () because Pluto is not in our solar system
print(bf("Neptune", "Mercury"))  # ==> () because Neptune comes after Mercury in the solar system
print(bf("Jupiter", "Jupiter"))  # ==> () because the input planets are the same
print(bf("Mars", "Mars"))  # ==> () because the input planets are the same
print(bf("Venus", "Venus"))  # ==> () because the input planets are the same
print(bf("Sun", "Mars"))  # ==> () because the input planets are not correct planet names
print(bf("Moon", "Earth"))  # ==> () because the input planets are not correct planet names
print(bf("Saturn", "Earth"))  # ==> ("Venus", "Mars")
print(bf("Uranus", "Saturn"))  # ==> ("Jupiter")
print(bf("Neptune", "Jupiter"))  # ==> ("Saturn", "Uranus")
print(bf("Venus", "Neptune"))  # ==> ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
print(bf("Mercury", "Saturn"))  # ==> ("Venus", "Earth", "Mars", "Jupiter")  # ==> ("Venus", "Earth", "Mars", "Jupiter")  # ==> ("Venus", "Earth", "Mars", "Jupiter")