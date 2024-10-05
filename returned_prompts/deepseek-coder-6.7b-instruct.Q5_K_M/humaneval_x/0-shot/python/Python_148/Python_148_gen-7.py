
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 > index2:
        index1, index2 = index2, index1
    return tuple(planets[index1+1:index2])

print(bf("Jupiter", "Neptune"))  # ➞ ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  # ips➞ ("Venus")
print(bf("Mercury", "Uranus"))  # ➞ ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Pluto", "Neptune"))  # ➞ ()
print(bf("Neptune", "Pluto"))  # ➞ ()
print(bf("Pluto", "Mercury"))  # ➞ ()
print(bf("Neptune", "Mercury"))  # ➞ ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")


'''
In the function `bf`, I first create a list of planets in order of their proximity to the sun.
Then I get the indices of the two input planets in this list. If the index of planet1 is greater than that of planet2, I swap them.
Finally, I return a tuple of all planets whose indices are between the indices of planet1 and planet2 (exclusive). 
If either of the planets are not in the list of planets, I return an empty tuple.
'''

#Testing with incorrect planets
print(bf("Pluto", "Neptune"))  # ➞ ()
print(bf("Mars", "Pluto"))  # ➞ ()
print(bf("Earth", "Pluto"))  # ➞ ()
<j