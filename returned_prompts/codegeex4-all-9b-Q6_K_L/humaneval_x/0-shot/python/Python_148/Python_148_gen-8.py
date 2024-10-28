def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        p1 = planets.index(planet1)
        p2 = planets.index(planet2)
    except ValueError:
        return ()
    if p1 > p2:
        p1, p2 = p2, p1
    return tuple(planets[p1+1:p2])

print(bf("Jupiter", "Neptune")) #==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury")) #==> ("Venus")
print(bf("Mercury", "Uranus")) #==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Earth", "Earth")) #==> ()
print(bf("Earth", "Pluto")) #==> ()
print(bf("Pluto", "Earth")) #==> ()

#test for the error handling
print(bf("Earth", 1)) #==> ()
print(bf("Earth", "Earth1")) #==> ()