def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    
    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index
    
    return tuple(planets[planet1_index + 1 : planet2_index])

print(bf("Jupiter", "Neptune")) # ==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury")) # ==> ("Venus")
print(bf("Mercury", "Uranus")) # ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")