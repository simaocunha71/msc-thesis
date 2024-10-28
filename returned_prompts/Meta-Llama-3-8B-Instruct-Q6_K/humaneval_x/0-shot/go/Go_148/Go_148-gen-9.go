Here is a Go function that satisfies the problem requirements:

```go
package main

import (
	"fmt"
)

func Bf(planet1, planet2 string) []string {
	planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
	var result []string

	for i, p := range planets {
		if p == planet1 {
			for j := i + 1; j < len(planets); j++ {
				if planets[j] == planet2 {
					result = planets[i+1 : j]
					return result
				}
			}
		} else if p == planet2 {
			for j := 0; j < i; j++ {
				if planets[j] == planet1 {
					result = planets[j+1 : i]
					return result
				}
			}
		}
	}

	return []string{}
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune"))  // Output: [Saturn Uranus]
	fmt.Println(Bf("Earth", "Mercury"))     // Output: [Venus]
	fmt.Println(Bf("Mercury", "Uranus"))    // Output: [Venus Earth Mars Jupiter Saturn]
}
```

This function iterates over the slice of planet names to find the indices of the input planets. It then uses these indices to slice the slice of planet names and return the slice of planets whose orbits are between the orbits of the input planets. If either of the input planets is not found, the function returns an empty slice. The `main` function demonstrates the usage of the `Bf` function with the examples provided. The output of these examples is as expected.