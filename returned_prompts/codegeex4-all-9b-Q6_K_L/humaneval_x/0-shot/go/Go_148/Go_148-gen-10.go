package main

import (
    "fmt"
    "strings"
)

var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

func Bf(planet1, planet2 string) []string {
    var result []string

    for i, planet := range planets {
        if planet == planet1 {
            for j := i + 1; j < len(planets); j++ {
                if planets[j] == planet2 {
                    return result
                }
                result = append(result, planets[j])
            }
        }
    }
    return result
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune"))
    fmt.Println(Bf("Earth", "Mercury"))
    fmt.Println(Bf("Mercury", "Uranus"))
}

```
