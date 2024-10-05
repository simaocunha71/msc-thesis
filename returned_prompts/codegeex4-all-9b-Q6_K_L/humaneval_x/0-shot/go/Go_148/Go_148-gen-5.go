package main

import (
    "fmt"
)

func Bf(planet1, planet2 string) []string {
    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    // Find the index of the planets in the planets slice
    var p1, p2 int
    for i, planet := range planets {
        if planet == planet1 {
            p1 = i
        }
        if planet == planet2 {
            p2 = i
        }
    }

    // If either planet is not found, return an empty slice
    if p1 == -1 || p2 == -1 {
        return []string{}
    }

    // Sort the planets between the two given planets
    var result []string
    if p1 < p2 {
        result = planets[p1+1 : p2]
    } else {
        result = planets[p2+1 : p1]
    }

    return result
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune")) // ==> ("Saturn", "Uranus")
    fmt.Println(Bf("Earth", "Mercury"))   // ==> ("Venus")
    fmt.Println(Bf("Mercury", "Uranus")) // ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
}
