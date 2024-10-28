
planet_names := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

// Check if planet1 and planet2 are valid
valid_planet1 := false
valid_planet2 := false

for _, planet := range planet_names {
    if planet == planet1 {
        valid_planet1 = true
    }
    if planet == planet2 {
        valid_planet2 = true
    }
}

if !valid_planet1 || !valid_planet2 {
    return []string{}
}

// Get the index of planet1 and planet2 in planet_names
index_planet1 := 0
index_planet2 := 0

for i, planet := range planet_names {
    if planet == planet1 {
        index_planet1 = i
    }
    if planet == planet2 {
        index_planet2 = i
    }
}

// Get the planets between planet1 and planet2
planets_between := planet_names[index_planet1+1 : index_planet2]

// Check if the order of planet1 and planet2 is not correct
if index_planet1 > index_planet2 {
    planets_between = append(planet_names[index_planet2+1:index_planet1], planets_between...)
}

return planets_between

}

func main()  {

fmt.Println(Bf("Jupiter", "Neptune")) //==> 应该输出 ("Saturn", "Uranus")
fmt.Println(Bf("Earth", "Mercury"))  //==> 应该输出 ("Venus")
fmt.Println(Bf("Mercury", "Uranus")) //==> 应该输出 ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

}

*/

package main

import (
	"fmt"
)

func Bf(planet1, planet2 string) []string {
	planets := []string