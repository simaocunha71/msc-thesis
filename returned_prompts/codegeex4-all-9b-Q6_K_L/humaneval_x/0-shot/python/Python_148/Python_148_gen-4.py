def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        p1 = planets.index(planet1)
        p2 = planets.index(planet2)
        if p1 > p2:
            return tuple(planets[p2:p1])
        else:
            return tuple(planets[p1:p2])
    except ValueError:
        return ()

print(bf("Jupiter", "Neptune"))  # ==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  # ==> ("Venus")
print(bf("Mercury", "Uranus"))  # ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")