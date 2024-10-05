
var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

if !contains(planets, planet1) || !contains(planets, planet2) {
	return nil
}

var result []string

for _, planet := range planets {
	if planet == planet1 || planet == planet2 {
		continue
	}

	if planet1 < planet && planet < planet2 {
		result = append(result, planet)
	}
}

return result

}

func contains(slice []string, target string) bool {
	for i := range slice {
		if slice[i] == target {
			return true
		}
	}

	return false
}





```

```go
package main

import "fmt"

func contains(slice []string, target string) bool {
	for i := range slice {
		if slice[i] == target {
			return true
		}
	}

	return false
}

func Bf(planet1, planet2 string) []string {
	var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

	if !contains(planets, planet1) || !contains(planets, planet2) {
		return nil
	}

	var result []string

	for _, planet := range planets {
		if planet == planet1 || planet == planet2 {
			continue
		}

		if planet1 < planet && planet < planet2 {
			result = append(result, planet)
		}
	}

	return result
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune"))
	fmt.Println(Bf("Earth", "Mercury"))
	fmt.Println(Bf("Mercury", "Uranus"))
}
```
```
