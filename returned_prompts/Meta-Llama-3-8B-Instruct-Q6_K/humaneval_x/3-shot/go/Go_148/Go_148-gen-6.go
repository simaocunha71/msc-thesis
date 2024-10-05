    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var result []string
    for _, p := range planets {
        if p == planet1 || p == planet2 {
            continue
        }
        if p == planet1 {
            for _, q := range planets {
                if q == planet2 {
                    result = append(result, q)
                }
            }
            return result
        }
        if p == planet2 {
            for i, q := range planets {
                if q == planet1 {
                    result = append(result, planets[i+1:i+5]...)
                    return result
                }
            }
        }
    }
    return result
}