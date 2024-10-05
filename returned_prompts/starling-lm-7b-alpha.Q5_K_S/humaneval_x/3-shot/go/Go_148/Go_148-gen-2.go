    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    if !contains(planets, planet1) || !contains(planets, planet2) {
        return []string{}
    }

    index1, index2 := findIndexes(planets, planet1, planet2)

    return planets[index1+1 : index2]
}

func findIndexes(planets []string, planet1, planet2 string) (int, int) {
    index1, index2 := -1, -1
    for i, p := range planets {
        if p == planet1 {
            index1 = i
        }
        if p == planet2 {
            index2 = i
        }
    }
    return index1, index2
}

func contains(planets []string, name string) bool {
    for _, p := range planets {
        if p == name {
            return true
        }
    }
    return false
}



