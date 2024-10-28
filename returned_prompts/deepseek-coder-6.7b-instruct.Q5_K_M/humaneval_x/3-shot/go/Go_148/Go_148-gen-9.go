    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    planet1_index := -1
    planet2_index := -1

    for i, planet := range planets {
        if planet == planet1 {
            planet1_index = i
        } else if planet == planet2 {
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



