    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    index1 := index(planets, planet1)
    index2 := index(planets, planet2)

    if index1 == -1 || index2 == -1 {
        return []string{}
    }
    result := []string{}
    for i := index1; i <= index2; i++ {
        result = append(result, planets[i])
    }
    return result
}

func index(planets []string, name string) int {
    for i := 0; i < len(planets); i++ {
        if planets[i] == name {
            return i
        }
    }
    return -1
}



