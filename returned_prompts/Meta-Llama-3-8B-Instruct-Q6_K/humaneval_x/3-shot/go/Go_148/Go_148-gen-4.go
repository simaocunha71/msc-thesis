    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    result := make([]string, 0)
    for _, p := range planets {
        if p == planet1 || p == planet2 {
            continue
        }
        index1, index2 := -1, -1
        for i, planet := range planets {
            if planet == planet1 {
                index1 = i
            }
            if planet == planet2 {
                index2 = i
            }
        }
        if index1 != -1 && index2 != -1 {
            for i := index1 + 1; i < index2; i++ {
                result = append(result, planets[i])
            }
        }
    }
    return result
}
