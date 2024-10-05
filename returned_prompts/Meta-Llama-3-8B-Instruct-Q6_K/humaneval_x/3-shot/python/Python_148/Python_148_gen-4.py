    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planets_sorted = sorted(planets)

    if planet1 not in planets_sorted or planet2 not in planets_sorted:
        return ()

    idx1 = planets_sorted.index(planet1)
    idx2 = planets_sorted.index(planet2)

    if idx2 < idx1:
        idx1, idx2 = idx2, idx1

    return tuple(planets_sorted[idx1:idx2+1])
    # or return tuple(sorted(planets_sorted[idx1:idx2+1])) to sort by proximity to the sun


