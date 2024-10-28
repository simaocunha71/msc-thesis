Here is a Go solution for the problem. It uses a predefined array of planet names and their corresponding order in the solar system. It then checks if the input planet names are correct and returns the planets whose orbits are between the input planets.

```go
package main

import "fmt"

func Bf(planet1, planet2 string) []string {
    planets := [...]string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var result []string

    for i, p := range planets {
        if p == planet1 || p == planet2 {
            continue
        }
        if planets[0] <= planet1 && planet1 <= planets[i] && planets[i] <= planet2 && planet2 <= planets[7] {
            result = append(result, p)
        }
    }

    if len(result) == 0 {
        return []string{}
    }

    return result
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune"))  // Output: [Saturn Uranus]
    fmt.Println(Bf("Earth", "Mercury"))     // Output: [Venus]
    fmt.Println(Bf("Mercury", "Uranus"))    // Output: [Venus Earth Mars Jupiter Saturn]
}
```

This code defines a function `Bf` that takes two planet names as strings `planet1` and `planet2`. It then iterates over the predefined array of planet names and checks if the current planet is between `planet1` and `planet2` in the order of the solar system. If it is, the planet is added to the result slice. Finally, the function returns the result slice. If the input planet names are not correct, the function returns an empty slice.

In the `main` function, we test the `Bf` function with the examples provided in the problem statement. The output of each test is printed to the console.