    planets  := [8]string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    result  := make([]string, 0)
    found_planet1, found_planet2 := false, false
    start_index, end_index := 0, 0

    for i, planet := range planets{
        if planet == planet1{
            found_planet1 = true
            start_index = i
            continue
        }

        if planet == planet2{
            found_planet2 = true
            end_index = i
            continue
        }
    }

    if !found_planet1 || !found_planet2{
        return result
    }

    if start_index > end_index{
        start_index, end_index = end_index, start_index
    }

    return planets[start_index+1 : end_index]
}

