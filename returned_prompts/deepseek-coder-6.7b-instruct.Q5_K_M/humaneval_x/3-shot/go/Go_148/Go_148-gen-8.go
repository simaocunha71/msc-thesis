    planets  := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    result  := make([]string, 0)

    var start_index, end_index int
    for i, planet  := range planets  {
        if planet == planet1  {
            start_index = i
        }
        if planet == planet2  {
            end_index = i
        }
    }
    if start_index > end_index  {
        start_index, end_index = end_index, start_index
    }

    if start_index != -1  && end_index != -1 {
        return planets[start_index + 1 : end_index]
    } else {
        return make([]string, 0)
    }
}



