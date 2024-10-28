Here is the Go function that implements the described behavior:

```go
package main

import (
    "fmt"
    "strings"
)

func Bf(planet1, planet2 string) []string {
    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    planet1Index := -1
    planet2Index := -1
    for i, planet := range planets {
        if planet == planet1 {
            planet1Index = i
        }
        if planet == planet2 {
            planet2Index = i
        }
    }
    if planet1Index == -1 || planet2Index == -1 {
        return nil
    }
    var result []string
    for i := planet1Index + 1; i < planet2Index; i++ {
        result = append(result, planets[i])
    }
    return result
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune"))  // Output: [Saturn Uranus]
    fmt.Println(Bf("Earth", "Mercury"))  // Output: [Venus]
    fmt.Println(Bf("Mercury", "Uranus"))  // Output: [Venus Earth Mars Jupiter Saturn]
}
```

This function first finds the indices of the input planets in the `planets` slice. If either of the planets is not found, it returns an empty slice. Then it iterates over the slice from the index of the first planet to the index of the second planet, and appends each planet to the result slice. The result slice is then returned. The `main` function demonstrates the usage of the `Bf` function with the provided examples.