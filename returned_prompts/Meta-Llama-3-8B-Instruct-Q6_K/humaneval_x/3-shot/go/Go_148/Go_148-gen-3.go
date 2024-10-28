    planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    planetIndex1, planetIndex2 := -1, -1
    for i, planet := range planets {
        if planet == planet1 {
            planetIndex1 = i
        }
        if planet == planet2 {
            planetIndex2 = i
        }
    }
    if planetIndex1 == -1 || planetIndex2 == -1 {
        return []string{}
    }
    if planetIndex1 > planetIndex2 {
        planetIndex1, planetIndex2 = planetIndex2, planetIndex1
    }
    result := planets[planetIndex1+1 : planetIndex2]
    return result
}