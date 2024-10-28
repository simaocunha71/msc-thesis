    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var start, end int
    var ok bool
    if start, ok = planet_to_index[planet1]; !ok {
        return []string{}
    }
    if end, ok = planet_to_index[planet2]; !ok {
        return []string{}
    }
    if start > end {
        start, end = end, start
    }
    return planets[start+1 : end]
}



