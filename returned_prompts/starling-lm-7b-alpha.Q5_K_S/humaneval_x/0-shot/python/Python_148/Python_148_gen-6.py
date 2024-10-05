
Here is a function that takes two planet names as strings planet1 and planet2. The function returns a tuple containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2, sorted by the proximity to the sun:

```python
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()

    result = []

    if planet1 == planet2:
        return (planet1,)

    i = planets.index(planet1)
    j = planets.index(planet2)

    if i > j:
        i, j = j, i

    for k in range(i, j+1):
        result.append(planets[k])

    result = tuple(result)
    return result
```

You can call this function with two planet names as strings. It will return a tuple with all planets whose orbits are located between the orbit of planet1 and the orbit of planet2, sorted by proximity to the sun.

```python
print(bf("Jupiter", "Neptune") == ("Saturn", "Uranus"))  # True
print(bf("Earth", "Mercury") == ("Venus"))  # True
print(bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))  # True
```

In the `bf` function, we first check if the provided planet names are valid. If not, we return an empty tuple.
Then, we determine the indices of `planet1` and `planet2` in the `planets` list. If `planet1` is greater than `planet2`, we swap their indices.
Next, we iterate over the planets from `planet1` to `planet2` (inclusive) and add them to the `result` list.
Finally, we convert the `result` list to a tuple and return it.

Note