    planets = [...]string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    i := -1
    j := -1
    for k, p := range planets {
        if p == planet1 {
            i = k
        }
        if p == planet2 {
            j = k
        }
        if i >= 0 && j >= 0 {
            result := planets[i+1:j]
            return result
        }
    }
    return []string{}
}