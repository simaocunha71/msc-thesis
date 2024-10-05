    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    planet1_index, planet2_index := -1, -1
    for i, v := range planets {
        if v == planet1 {
            planet1_index = i
        }
        if v == planet2 {
            planet2_index = i
        }
    }
    if planet1_index == -1 || planet2_index == -1 {
        return []string{}
    }
    if planet1_index > planet2_index {
        planet1_index, planet2_index = planet2_index, planet1_index
    }
    return planets[planet1_index+1 : planet2_index]
}



