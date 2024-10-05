    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    index1 := -1
    index2 := -1
    for i, p := range planets {
        if p == planet1 {
            index1 = i
        } else if p == planet2 {
            index2 = i
        }
    }

    if index1 == -1 || index2 == -1 {
        return []string{}
    }

    result := make([]string, index2 - index1)
    for i := index1; i < index2; i++ {
        result[i-index1] = planets[i]
    }

    return result
}



