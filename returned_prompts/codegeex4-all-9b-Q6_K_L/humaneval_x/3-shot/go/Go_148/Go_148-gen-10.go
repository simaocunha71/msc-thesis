    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    if !contains(planets, planet1) || !contains(planets, planet2) {
        return []string{}
    }

    var start, end int
    for i, planet := range planets {
        if planet == planet1 {
            start = i
        }
        if planet == planet2 {
            end = i
        }
    }

    if start > end {
        start, end = end, start
    }

    return planets[start+1 : end]
}

func contains(slice []string, item string) bool {
    for _, a := range slice {
        if a == item {
            return true
        }
    }
    return false
}



