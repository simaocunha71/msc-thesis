
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets:
        return ()
    if planet2 not in planets:
        return ()
    if planet1 == planet2:
        return (planet1, )
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    res = []
    for i in range(idx1, idx2 + 1):
        res.append(planets[i])
    return tuple(res)

# def bf(planet1, planet2):
#     planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#     if planet1 not in planets or planet2 not in planets:
#         return ()
#     idx1 = planets.index(planet1)
#     idx2 = planets.index(planet2)
#     res = []
#     for i in range(idx1, idx2