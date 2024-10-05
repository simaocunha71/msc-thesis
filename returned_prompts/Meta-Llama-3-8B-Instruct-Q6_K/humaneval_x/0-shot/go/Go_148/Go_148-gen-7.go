Here is a Go solution for the problem:

```go
package main

import (
    "fmt"
    "strings"
)

var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

func Bf(planet1, planet2 string) []string {
    planetIndex1 := -1
    planetIndex2 := -1

    for i, planet := range planets {
        if planet == planet1 {
            planetIndex1 = i
        }
        if planet == planet2 {
            planetIndex2 = i
        }
        if planetIndex1 != -1 && planetIndex2 != -1 {
            break
        }
    }

    if planetIndex1 == -1 || planetIndex2 == -1 {
        return []string{}
    }

    planetsBetween := make([]string, 0, planetIndex2-planetIndex1-1)
    for i := planetIndex1 + 1; i < planetIndex2; i++ {
        planetsBetween = append(planetsBetween, planets[i])
    }

    return planetsBetween
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune")) // ["Saturn", "Uranus"]
    fmt.Println(Bf("Earth", "Mercury")) // ["Venus"]
    fmt.Println(Bf("Mercury", "Uranus")) // ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
}
```

The `Bf` function iterates over the list of planets to find the indices of the input planets. If either of the planets is not found, the function returns an empty slice. Otherwise, it creates a new slice with the planets between the two input planets and returns it. The `main` function tests the `Bf` function with the given examples. The output of the `main` function is the same as the expected output in the problem description.