```go
package kata

import (
	"strings"
)

func Bf(planet1, planet2 string) []string {
	var planets []string
	planets = append(planets, "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
	if !contains(planets, strings.Title(planet1)) || !contains(planets, strings.Title(planet2)) {
		return []string{}
	}
	if strings.Title(planet1) == strings.Title(planet2) {
		return []string{}
	}
	if strings.Index(planets, strings.Title(planet1)) > strings.Index(planets, strings.Title(planet2)) {
		planet1, planet2 = planet2, planet1
	}
	var result []string
	for _, planet := range planets {
		if strings.Index(planets, planet) > strings.Index(planets, strings.Title(planet1)) && strings.Index(planets, planet) < strings.Index(planets, strings.Title(planet2)) {
			result = append(result, planet)
		}
	}
	return result
}

func contains(arr []string, str string) bool {
	for _, a := range arr {
		if a == str {
			return true
		}
	}
	return false
}

func main() {
	println(Bf("Jupiter", "Neptune"))
	println(Bf("Earth", "Mercury"))
	println(Bf("Mercury", "Uranus"))
}
```
