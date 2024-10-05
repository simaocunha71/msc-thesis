    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    index1 := -1
    index2 := -1

    for i, planet := range planets {
        if planet == planet1 {
            index1 = i
        } else if planet == planet2 {
            index2 = i
        }
    }

    if index1 == -1 || index2 == -1 {
        return []string{}
    }

    if index1 > index2 {
        index1, index2 = index2, index1
    }

    return planets[index1+1 : index2]
}

