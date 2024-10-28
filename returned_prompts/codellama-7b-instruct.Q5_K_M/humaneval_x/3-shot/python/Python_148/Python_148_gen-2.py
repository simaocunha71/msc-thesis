    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 == index2:
        return ()
    elif index1 > index2:
        return (planets[index1+1:index2+1])
    else:
        return (planets[index2+1:index1+1])


