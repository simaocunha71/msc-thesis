    var result = make([]string,0)
    var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var index1 = -1
    var index2 = -1
    for i, v := range planets {
        if v == planet1 {
            index1 = i
        }
        if v == planet2 {
            index2 = i
        }
    }
    if index1 == -1 || index2 == -1 {
        return result
    }

    if index1 == 0 {
        for i := index1 + 1; i <= index2; i++ {
            result = append(result, planets[i])
        }
        return result
    }

    if index2 == len(planets)-1 {
        for i := index1; i < index2; i++ {
            result = append(result, planets[i])
        }
        return result
    }

    if index1 > index2 {
        for i := index1; i >= index2; i-- {
            result = append(result, planets[i])
        }
        for i := index1 - 1; i >= 0; i-- {
            result = append(result, planets[i])
        }
    } else {
        for i := index1; i <= index2; i++ {
            result = append(result, planets[i])
        }
    }
    return result
}



