
package main

import "fmt"

func main() {
	fmt.Println(Bf("Jupiter", "Neptune"))
	fmt.Println(Bf("Earth", "Mercury"))
	fmt.Println(Bf("Mercury", "Uranus"))
}

func Bf(planet1, planet2 string) []string {
	planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
	if !contains(planets, planet1) || !contains(planets, planet2) {
		return []string{}
	}
	start := index(planets, planet1)
	end := index(planets, planet2)
	ret := []string{}
	for i := start; i <= end; i++ {
		ret = append(ret, planets[i])
	}
	return ret
}

func contains(slice []string, target string) bool {
	for _, v := range slice {
		if v == target {
			return true
		}
	}
	return false
}

func index(slice []string, target string) int {
	for i, v := range slice {
		if v == target {
			return i
		}
	}
	return -1
}



















































































































































































