
	planetList := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
	result := []string{}

	// Check if both planets are in the list
	if !contains(planetList, planet1) || !contains(planetList, planet2) {
		return result
	}

	// Get the index of both planets
	index1 := getIndex(planetList, planet1)
	index2 := getIndex(planetList, planet2)

	// If the index1 is larger than index2, swap them
	if index1 > index2 {
		index1, index2 = index2, index1
	}

	// Add planets between planet1 and planet2 to result
	for i := index1 + 1; i < index2; i++ {
		result = append(result, planetList[i])
	}

	return result
}

// Helper function to check if a slice contains a specific element
func contains(slice []string, element string) bool {
	for _, v := range slice {
		if v == element {
			return true
		}
	}
	return false
}

// Helper function to get the index of an element in a slice
func getIndex(slice []string, element string) int {
	for i, v := range slice {
		if v == element {
			return i
		}
	}
	return -1
}

*/

import "sort"

func Bf(planet1, planet2 string) (res []string) {
	planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}

	// Check if both planets are in the list
	sort.Strings(planets)
	index1 := sort.SearchStrings(planets, planet1)
	index2 := sort.SearchStrings(planets, planet2)

	if index1 == len(planets) || planets[index1] != planet1 || index2 == len(planets) || planets[index2] !