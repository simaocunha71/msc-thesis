package main

import (
	"fmt"
)

var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

func Bf(planet1, planet2 string) []string {

	for i, planet := range planets {
		if planet == planet1 {
			for j := i + 1; j < len(planets); j++ {
				if planets[j] == planet2 {
					return planets[i+1 : j]
				}
			}
		}
	}

	return nil
}

func main() {
	fmt.Println(Bf("Jupiter", "Neptune"))   // ==> ("Saturn", "Uranus")
	fmt.Println(Bf("Earth", "Mercury"))     // ==> ("Venus")
	fmt.Println(Bf("Mercury", "Uranus"))    // ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
	fmt.Println(Bf("Earth", "Pluto"))      // ==> nil
}