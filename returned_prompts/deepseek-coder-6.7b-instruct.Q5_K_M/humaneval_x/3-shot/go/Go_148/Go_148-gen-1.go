    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var start, end int
    var ok1, ok2 bool

    for i, planet := range planets {
        if planet == planet1 {
            start = i
            ok1 = true
        }
        if planet == planet2 {
            end = i
            ok2 = true
        }
    }

    if !ok1 || !ok2 {
        return []string{}
    }

    if start > end {
        start, end = end, start
    }

    return planets[start+1 : end]
}



