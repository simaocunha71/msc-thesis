    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    return tuple(planets[index1+1:index2]) if index1 < index2 else tuple(planets[index2+1:index1])  # Sort the result by proximity to the sun. This is already the case if the planets are in the same order as in the list. If they are not, we need to reverse the result.
    



