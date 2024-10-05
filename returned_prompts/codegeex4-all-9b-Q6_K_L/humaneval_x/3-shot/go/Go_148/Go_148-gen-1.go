    var planets []string = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var planet1_index, planet2_index int

    for i, planet := range planets {
        if planet == planet1 {
            planet1_index = i
        }
        if planet == planet2 {
            planet2_index = i
        }
    }
    if planet1_index == -1 || planet2_index == -1 {
        return make([]string, 0)
    }

    var result []string
    if planet1_index < planet2_index {
        for i := planet1_index + 1; i < planet2_index; i++ {
            result = append(result, planets[i])
        }
    } else {
        for i := planet2_index + 1; i < planet1_index; i++ {
            result = append(result, planets[i])
        }
    }
    return result
}

