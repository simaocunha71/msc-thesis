    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    var result []string
    for i, p := range planets {
        if p == planet1 || p == planet2 {
            if i == 0 && p == planet1 {
                result = append(result, planets[i+1:]...)
            }
            if i == len(planets)-1 && p == planet2 {
                result = append(result, planets[:i]...)
            }
            if i != 0 && i != len(planets)-1 {
                result = append(result, planets[:i]...)
                result = append(result, planets[i+1:]...)
            }
        }
    }
    return result
}



