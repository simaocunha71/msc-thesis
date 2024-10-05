    planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    planet1Index := -1
    planet2Index := -1

    for i, planet := range planets {
        if planet == planet1 {
            planet1Index = i
        }
        if planet == planet2 {
            planet2Index = i
        }
    }

    if planet1Index == -1 || planet2Index == -1 {
        return []string{}
    }

    result := make([]string, 0)
    for i := planet1Index + 1; i < planet2Index; i++ {
        result = append(result, planets[i])
    }

    return result
}