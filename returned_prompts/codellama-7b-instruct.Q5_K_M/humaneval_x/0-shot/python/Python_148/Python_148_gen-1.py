
def bf(planet1, planet2):
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        return sorted(
            planets[planet1:planet2+1],
            key=lambda p: planets.index(p))

planets = (
    "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
)
