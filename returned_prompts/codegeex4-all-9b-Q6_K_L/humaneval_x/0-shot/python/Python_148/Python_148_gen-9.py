def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    p1, p2 = planets.index(planet1), planets.index(planet2)
    if p1 > p2:
        p1, p2 = p2, p1
    return tuple(planets[p1+1:p2])

print(bf("Jupiter", "Neptune")) #==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury")) #==> ("Venus")
print(bf("Mercury", "Uranus")) #==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")