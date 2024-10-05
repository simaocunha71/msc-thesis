
The function `bf(planet1, planet2)` takes two planet names as strings and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by the proximity to the sun. If `planet1` or `planet2` are not correct planet names, the function returns an empty tuple.

Here is the Python code for the function:

```Python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()

    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)

    if idx1 > idx2:
        idx1, idx2 = idx2, idx1

    return tuple(planets[idx1+1:idx2+1])
```
Here's how it works:

1. First, it checks if `planet1` and `planet2` are valid planet names. If either is not a valid planet name, it returns an empty tuple.
2. It then finds the index of `planet1` and `planet2` in the list of planets.
3. If `planet1` is located after `planet2`, it swaps their indices so that `planet1` is always the earlier planet.
4. Finally, it returns a tuple containing all planets between `planet1` and `planet2`, inclusive, in the correct order. The `idx1+1:idx2+1` slice of the `planets` list returns a list of planets, which is then converted to a tuple using the `tuple()` function.