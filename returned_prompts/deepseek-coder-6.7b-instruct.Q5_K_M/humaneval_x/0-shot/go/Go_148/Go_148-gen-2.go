
    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var result []string

    // Check if planets are valid
    for _, planet := range []string{planet1, planet2} {
        if !contains(planets, planet) {
            return []string{}
        }
    }

    // Find the index of planet1 and planet2
    index1, index2 := findIndex(planets, planet1), findIndex(planets, planet2)

    if index1 > index2 {
        index1, index2 = index2, index1
    }

    for i := index1 + 1; i < index2; i++ {
        result = append(result, planets[i])
    }

    return result
}

func contains(s []string, str string) bool {
    for _, v := range s {
        if v == str {
            return true
        }
    }

    return false
}

func findIndex(s []string, str string) int {
    for i, v := range s {
        if v == str {
            return i
        }
    }

    return -1
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune")) //==> “Saturn", "Uranus"
    fmt.Println(Bf("Earth", "Mercury")) //==> “Venus"
    fmt.Println(Bf("Mercury", "Uranus")) //==> “Venus", "Earth", "Mars", "Jupiter", "Saturn"
}
```

This script checks if planet1 and planet2 are valid planets in the solar system, then finds their indexes. It ensures that index1 is always the smaller one, then iterates from index1+1 to index2 (exclusive) adding each planet to the result slice. It finally returns the result slice.

If either planet1 or planet2 is not a valid planet, the function returns an empty slice.

Please note that the planets are