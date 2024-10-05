
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
        if idx1 < idx2:
            return tuple(planets[idx1+1:idx2])
        else:
            return tuple(planets[idx2+1:idx1])

print(bf("Jupiter", "Neptune"))  #==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  #==> ("Venus")
print(bf("Mercury", "Uranus"))  #==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Pluto", "Neptune"))  #==> ()


The function bf takes in two planet names as strings. It first checks if the planet names are valid by seeing if they are in the list of planets. If they are not, it returns an empty tuple. If the planets are valid, it finds the index of both planets in the list of planets. It then returns a tuple of all planets between the two indexes, sorted by proximity to the sun.
<jupyter_output>
<empty_output>
<jupyter_text>
