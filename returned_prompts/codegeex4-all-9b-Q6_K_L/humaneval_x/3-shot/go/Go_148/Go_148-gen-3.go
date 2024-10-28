    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    result := make([]string, 0)
    for i := 0; i < len(planets); i++ {
        if planets[i] == planet1 {
            for j := i + 1; j < len(planets); j++ {
                if planets[j] == planet2 {
                    for k := i + 1; k < j; k++ {
                        result = append(result, planets[k])
                    }
                    return result
                }
            }
        } else if planets[i] == planet2 {
            for j := i - 1; j > -1; j-- {
                if planets[j] == planet1 {
                    for k := j + 1; k < i; k++ {
                        result = append(result, planets[k])
                    }
                    return result
                }
            }
        }
    }
    return result
}


