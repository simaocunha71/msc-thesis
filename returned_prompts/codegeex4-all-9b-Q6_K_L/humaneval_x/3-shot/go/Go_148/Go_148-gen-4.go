    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    for i, planet := range planets {
        if planet == planet1 {
            for j := i + 1; j < len(planets); j++ {
                if planets[j] == planet2 {
                    return planets[i+1 : j]
                }
            }
        }
    }

    return []string{}
}

