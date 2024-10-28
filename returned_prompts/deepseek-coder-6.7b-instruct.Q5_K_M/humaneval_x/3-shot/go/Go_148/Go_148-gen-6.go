    planets_order := []string{
        "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune",
    }

    var start, end int
    var found bool

    for i, planet := range planets_order {
        if planet == planet1 {
            start = i
            found = true
        }
        if planet == planet2 {
            end = i
            found = true
        }
    }

    if !found || start > end {
        return []string{}
    }

    return planets_order[start+1 : end]
}



