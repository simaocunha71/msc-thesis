    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    index1 := index(planets, planet1)
    index2 := index(planets, planet2)
    if index1 == -1 || index2 == -1 {
        return []string{}
    }
    result := make([]string, 0)
    for i := index1; i <= index2; i++ {
        result = append(result, planets[i])
    }
    return result
}

func index(planets []string, name string) int {
    for i, p := range planets {
        if p == name {
            return i
        }
    }
    return -1
}



