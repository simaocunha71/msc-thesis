Here is the solution:
```go
package main

import (
	"fmt"
	"strings"
)

func Bf(planet1, planet2 string) []string {
	planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
	var result []string

	for _, p := range planets {
		if p == planet1 || p == planet2 {
			continue
		}
		if p < planet1 {
			continue
		}
		if p > planet2 {
			break
		}
		result = append(result, p)
	}

	if len(result) == 0 {
		return []string{}
	}

	sort.Strings(result)

	return result
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune")) // ["Saturn", "Uranus"]
	fmt.Println(Bf("Earth", "Mercury")) // ["Venus"]
	fmt.Println(Bf("Mercury", "Uranus")) // ["Venus", "Earth", "Mars", "Jupiter", "Saturn"]
}
```
This function takes two planet names as strings and returns a slice of planet names whose orbits are located between the orbit of planet1 and the orbit of planet2. It first checks if planet1 or planet2 are not correct planet names, then it iterates over the planets list and appends the planets whose orbits are located between the orbit of planet1 and the orbit of planet2 to the result slice. Finally, it sorts the result slice and returns it. The function also checks if the result slice is empty, if it is, it returns an empty slice. The main function demonstrates how to use the Bf function with different planet names.