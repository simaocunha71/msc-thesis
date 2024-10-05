
	// If either planet is not valid, return empty tuple
	if !isValidPlanet(planet1) || !isValidPlanet(planet2) {
		return []string{}
	}

	// Find index of planet1 and planet2 in the list of planets
	var planet1Idx, planet2Idx int
	for i := range planets {
		if planets[i] == planet1 {
			planet1Idx = i
		}
		if planets[i] == planet2 {
			planet2Idx = i
		}
	}

	// Find the midpoint of the two planets' orbits
	midpoint := (planet1Idx + planet2Idx) / 2

	// Find all planets between planet1 and planet2, sorted by proximity to the sun
	var sortedPlanets []string
	for i := range planets {
		if i >= planet1Idx && i <= planet2Idx {
			sortedPlanets = append(sortedPlanets, planets[i])
		}
	}
	sort.Strings(sortedPlanets)

	return sortedPlanets
}

// Check if a string is a valid planet name
func isValidPlanet(planet string) bool {
	switch planet {
	case "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune":
		return true
	default:
		return false
	}
}

// Planets in our solar system
var planets = []string{
	"Mercury",
	"Venus",
	"Earth",
	"Mars",
	"Jupiter",
	"Saturn",
	"Uranus",
	"Neptune",
}
