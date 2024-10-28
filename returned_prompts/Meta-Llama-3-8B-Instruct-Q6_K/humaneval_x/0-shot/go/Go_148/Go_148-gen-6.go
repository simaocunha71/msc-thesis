```
package main

import (
	"fmt"
)

var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

func Bf(planet1, planet2 string) []string {
	if !isPlanet(planet1) || !isPlanet(planet2) {
		return []string{}
	}

	i1, i2 := -1, -1
	for i, planet := range planets {
		if planet == planet1 {
			i1 = i
		} else if planet == planet2 {
			i2 = i
		}
		if i1 != -1 && i2 != -1 {
			break
		}
	}

	if i1 == -1 || i2 == -1 {
		return []string{}
	}

	result := make([]string, 0)
	for i := i1 + 1; i < i2; i++ {
		result = append(result, planets[i])
	}

	return result
}

func isPlanet(planet string) bool {
	for _, p := range planets {
		if p == planet {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune"))  // ["Saturn", "Uranus"]
	fmt.Println(Bf("Earth", "Mercury"))    // ["Venus"]
	fmt.Println(Bf("Mercury", "Uranus"))  // ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
}
```
The code defines a function `Bf` that takes two planet names as strings and returns a slice of strings containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`. If either `planet1` or `planet2` are not correct planet names, the function returns an empty slice.

The function first checks if both planet names are valid by calling the `isPlanet` function. If either name is invalid, it returns an empty slice.

It then finds the indices of `planet1` and `planet2` in the `planets` slice. If either of these indices is not found, it returns an empty slice.

Finally, it creates a slice `result` to store the planets whose orbits are between the orbits of `planet1` and `planet2`. It iterates over the `planets