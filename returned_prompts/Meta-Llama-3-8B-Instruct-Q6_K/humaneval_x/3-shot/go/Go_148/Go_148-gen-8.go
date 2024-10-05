    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    i1, i2 := -1, -1
    for i, planet := range planets {
        if planet == planet1 {
            i1 = i
        }
        if planet == planet2 {
            i2 = i
        }
    }
    if i1 == -1 || i2 == -1 {
        return []string{}
    }
    result := planets[i1+1 : i2]
    return result
}