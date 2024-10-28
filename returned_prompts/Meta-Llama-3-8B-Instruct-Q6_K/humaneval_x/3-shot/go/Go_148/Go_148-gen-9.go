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
    result := make([]string, 0)
    for i := planetIndex1 + 1; i < planetIndex2; i++ {
        result = append(result, planets[i])
    }
    return result
}