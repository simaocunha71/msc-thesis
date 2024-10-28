package main

import "fmt"

func Bf(planet1, planet2 string) []string {
    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

    index1, index2 := -1, -1
    for i, planet := range planets {
        if planet == planet1 {
            index1 = i
        }
        if planet == planet2 {
            index2 = i
        }
    }

    if index1 == -1 || index2 == -1 {
        return []string{}
    }

    start, end := 0, len(planets)-1
    if index1 > index2 {
        start, end = end, start
    }

    return planets[start+1 : end]
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune")) // Output: ["Saturn", "Uranus"]
    fmt.Println(Bf("Earth", "Mercury"))   // Output: ["Venus"]
    fmt.Println(Bf("Mercury", "Uranus"))  // Output: ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
}
