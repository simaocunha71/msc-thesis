package main

import (
    "fmt"
)

var planets = map[string]int{
    "Mercury": 1,
    "Venus":   2,
    "Earth":   3,
    "Mars":    4,
    "Jupiter": 5,
    "Saturn":  6,
    "Uranus":  7,
    "Neptune": 8,
}

func Bf(planet1, planet2 string) []string {
    if _, ok := planets[planet1]; !ok || _, ok = planets[planet2]; !ok {
        return []string{}
    }

    start, end := planets[planet1], planets[planet2]
    if start > end {
        start, end = end, start
    }

    var result []string
    for i := start + 1; i < end; i++ {
        for planet, index := range planets {
            if index == i {
                result = append(result, planet)
                break
            }
        }
    }

    return result
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune")) // Output: ["Saturn", "Uranus"]
    fmt.Println(Bf("Earth", "Mercury"))   // Output: ["Venus"]
    fmt.Println(Bf("Mercury", "Uranus")) // Output: ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
}
