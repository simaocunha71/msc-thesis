
// Code your function here

}

// Test cases
fmt.Println(Bf("Jupiter", "Neptune")) //==> ⟨"Saturn", "Uranus"⟩
fmt.Println(Bf("Earth", "Mercury")) //==> ⟨"Venus"⟩
fmt.Println(Bf("Mercury", "Uranus")) //==> ⟨"Venus", "Earth", "Mars", "Jupiter", "Saturn"⟩
fmt.Println(Bf("Pluto", "Neptune")) //==> ⟨⟩
fmt.Println(Bf("Jupiter", "Pluto")) //==> ⟨⟩
*/

package main

import (
	"fmt"
	"sort"
)

var planets = map[string]int{
	"Mercury": 1,
	"Venus":   2,
	"Earth":   3,
	"Mars":    4,
	"Jupiter": 5,
	"Saturn":  6,
	"Uranus":  7,
	"Neptune": 8,
}

func Bf(planet1, planet2 string) []string {

	sort.Slice(planet, func(i, j int) bool {
		return planets[planet[i]] < planets[planet2]
	})

	start, end := planets[planet1], planets[planet2]
	if start > end {
		start, end = end, start
	}

	result := make([]string, 0)
	for name, distance := range planets {
		if distance > start && distance < end {
			result = append(result, name)
		}
	}
	return result
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune")) //==> ⟨"Saturn", "Uranus"⟩
	fmt.Println(Bf("Earth", "Mercury"))  //==> ⟨"Venus"