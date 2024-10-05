    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var result []string
    for _, planet := range planets {
        if planet == planet1 || planet == planet2 {
            continue
        }
        if planet1 < planet && planet < planet2 {
            result = append(result, planet)
        }
    }
    return result
}



