
def bf(planet1, planet2):
    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
        return tuple(planets[idx1+1:idx2+1])
