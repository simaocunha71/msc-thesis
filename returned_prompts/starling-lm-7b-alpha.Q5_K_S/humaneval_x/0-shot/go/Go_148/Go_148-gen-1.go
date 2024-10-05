
Here is one possible solution:

```go
package main

import (
	"fmt"
)

func planetsBetween(planet1, planet2 string) []string {
	planets := []string{
		"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune",
	}
	index1 := findIndex(planets, planet1)
	index2 := findIndex(planets, planet2)
	if index1 == -1 || index2 == -1 {
		return []string{}
	}
	result := []string{}
	for i := index1; i < index2; i++ {
		result = append(result, planets[i])
	}
	return result
}

func findIndex(planets []string, planet string) int {
	for i, p := range planets {
		if p == planet {
			return i
		}
	}
	return -1
}

func main() {
	fmt.Println(planetsBetween("Jupiter", "Neptune"))
	fmt.Println(planetsBetween("Earth", "Mercury"))
	fmt.Println(planetsBetween("Mercury", "Uranus"))
}
```

In this solution, the function `planetsBetween` takes two planet names as strings `planet1` and `planet2`. It first creates a slice of planets with their names and finds the indexes of `planet1` and `planet2` in the slice using the `findIndex` helper function. If either index is -1 (which means the planet is not in the slice), the function returns an empty slice. Otherwise, it creates a result slice, iterates from `index1` to `index2`, and appends the corresponding planets to the result slice. Finally, the function returns the result slice.

The `findIndex` helper function iterates over the planets slice and checks if the planet at index `i` matches the given planet. If it does, the function returns the index; otherwise, it returns -1.

In the `main` function, three test cases are provided to