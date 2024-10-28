func Bf(planet1, planet2 string) []string {
	planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
	for i := 0; i < len(planets); i++ {
		if planets[i] == planet1 {
			for j := i + 1; j < len(planets); j++ {
				if planets[j] == planet2 {
					return planets[i+1 : j]
				}
			}
		}
	}
	return nil
}