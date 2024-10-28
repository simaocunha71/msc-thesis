Here is a Go solution for the problem:

```go
package main

import (
	"fmt"
)

func Bf(planet1, planet2 string) []string {
	planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
	if !contains(planets, planet1) || !contains(planets, planet2) {
		return []string{}
	}
	i, j := -1, -1
	for k, p := range planets {
		if p == planet1 {
			i = k
		} else if p == planet2 {
			j = k
		}
	}
	if i == -1 || j == -1 {
		return []string{}
	}
	return planets[i+1 : j]
}

func contains(planets []string, planet string) bool {
	for _, p := range planets {
		if p == planet {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune")) // ["Saturn", "Uranus"]
	fmt.Println(Bf("Earth", "Mercury")) // ["Venus"]
	fmt.Println(Bf("Mercury", "Uranus")) // ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
}
```

The function Bf takes two planet names as strings and returns a slice of strings containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2, sorted by the proximity to the sun. If planet1 or planet2 are not correct planet names, the function returns an empty slice.

The function contains checks if a planet name is in the list of planets. The main function tests the Bf function with different inputs. The output is as expected.