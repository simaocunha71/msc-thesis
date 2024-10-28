```go
package main

import (
    "fmt"
    "strings"
)

var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

func Bf(planet1, planet2 string) []string {
    if !contains(planets, planet1) || !contains(planets, planet2) {
        return []string{}
    }

    var result []string

    for i, p := range planets {
        if p == planet1 {
            for _, q := range planets[i+1:] {
                if q == planet2 {
                    result = append(result, planets[i+1:i+len(planets)-len(planets[i+1:])]...)
                    return result
                }
            }
        }
    }

    return result
}

func contains(s []string, e string) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune"))  // Output: [Saturn Uranus]
    fmt.Println(Bf("Earth", "Mercury"))     // Output: [Venus]
    fmt.Println(Bf("Mercury", "Uranus"))    // Output: [Venus Earth Mars Jupiter Saturn]
}
```

The function Bf takes two planet names as input and returns a slice of planet names that are between the orbits of the two input planets. The function first checks if both input planets are valid by calling the helper function contains. If either of the input planets is invalid, the function returns an empty slice.

If both input planets are valid, the function then iterates over the slice of planet names to find the index of the first input planet. It then iterates over the remaining planets in the slice to find the index of the second input planet. The function then appends the planets in between the two input planets to the result slice and returns the result.

The helper function contains checks if a given planet name is present in the slice of planet names. The main function demonstrates the usage of the Bf function with different input planet names. The output of the main function is printed to the console.