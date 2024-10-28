
The function `bf(planet1, planet2)` takes two planet names as strings and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by the proximity to the sun.

First, the function checks if `planet1` and `planet2` are correct planet names by verifying if they are in the list of planets. If either `planet1` or `planet2` is not in the list, the function returns an empty