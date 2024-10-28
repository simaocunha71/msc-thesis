
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        index1, index2 = planets.index(planet1), planets.index(planet2)
        if index1 > index2:
            index1, index2 = index2, index1
        return tuple(planets[index1+1:index2])

print(bf("Jupiter", "Neptune"))  #==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  #==> ("Venus")
print(bf("Mercury", "Uranus"))  #==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Pluto", "Neptune"))  #==> ()
print(bf("Jupiter", "Pluto"))  #==> ()
print(bf("Jupiter", "Earth"))  #==> ()


In this solution, I used Python's list index() method to get the indexes of the planets. Then I sorted these indexes and used slicing to get the planets between them.
If either of the planet names is not found in the list of planet names, the function returns an empty tuple.
'''


def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        return tuple(sorted(planets[planets.index(planet1):planets.index(planet2)+1], key=planets.index))
    except ValueError:
        return ()

print(bf("Jupiter", "Neptune"))  #==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  #==> ("Venus")
print(bf("Mercury", "Uranus"))  #