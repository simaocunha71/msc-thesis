
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
        res = ()
        for i in range(idx1, idx2 + 1):
            res += (planets[i],)
        return tuple(res)


# Alternative solution with list comprehension
# def bf(planet1, planet2):
#     planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#     idx1 = planets.index(planet1)
#     idx2 = planets.index(planet2)
#     return tuple(planets[i] for i in range(idx1, idx2 + 1))

# Alternative solution with generator
# def bf(planet1, planet2):
#     planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#     idx1 = planets.index(planet1)
#     idx2 = planets.index(planet2)
#     return tuple(p for i, p in enumerate(planets) if i >= idx1 and i <= idx2)

# Alternative solution with filter()
# def bf(planet1, planet2):
#     planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#     idx1 = planets.index(planet1)
#     idx2 = planets.index(planet2)
#     return tuple(filter(lambda i: i >= idx1 and i <= idx2, range(len(planets))))

# Alternative solution with itertools.takewhile() and itertools