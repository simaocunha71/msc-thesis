    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    result := make([]string, 0)
    for _, p := range planets {
        if p == planet1 || p == planet2 {
            continue
        }
        if p > planet1 && p < planet2 {
            result = append(result, p)
        }
    }
    return result
}



