    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    result := make([]string, 0)

    for i, planet := range planets {
        if planet == planet1 {
            if i > 0 {
                result = append(result, planets[:i]...)
            }
            if i < len(planets) {
                result = append(result, planets[i:]...)
            }
            return result
        } else if planet == planet2 {
            if i > 0 {
                result = append(result, planets[:i]...)
            }
            return result
        }
    }

    return result
}



