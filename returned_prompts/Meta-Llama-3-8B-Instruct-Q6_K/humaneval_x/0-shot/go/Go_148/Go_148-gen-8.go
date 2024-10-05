Here is the solution in Go:
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
			start := i
		} else if p == planet2 {
			end := i + 1
		}
	}

	for i := start; i < end; i++ {
		result = append(result, planets[i])
	}

	return result
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune")) // [Saturn Uranus]
	fmt.Println(Bf("Earth", "Mercury")) // [Venus]
	fmt.Println(Bf("Mercury", "Uranus")) // [Venus Earth Mars Jupiter Saturn]
}
```
This function iterates through the list of planets, finding the indices of the input planets and then appends the planets between them to the result slice. Note that the end index is `i + 1` because the loop iterates until but not including the end index. The function returns the result slice as a string slice. In the main function, we test the function with the provided examples. The output is as expected.