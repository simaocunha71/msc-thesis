The problem can be solved by creating a list of planets in the correct order and then checking if both planet1 and planet2 are in the list. If they are, we can find their positions in the list and then return a tuple containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2.

Here is the Python code for the solution:

```
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    return tuple(planets[index1+1:index2])
```

This function works by first checking if both planet1 and planet2 are in the list of planets. If not, it returns an empty tuple. If they are, it finds their positions in the list using the index method, and then returns a tuple containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2. The slice notation [index1+1:index2] is used to get the planets in the correct order. The function returns a tuple because the problem statement asks for a tuple. If you want to return a list instead, you can replace tuple with list. 





The time complexity of this function is O(n), where n is the number of planets in the list, because we are using the index method to find the positions of planet1 and planet2 in the list, and the slice notation to create the tuple of planets. The space complexity is O(1), because we are using a constant amount of space to store the list of planets and the tuple of planets.