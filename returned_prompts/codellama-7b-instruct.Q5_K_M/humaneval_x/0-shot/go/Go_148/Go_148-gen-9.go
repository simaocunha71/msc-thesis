
// Bf("Earth", "Mercury") ==> ("Venus")
// Bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
// Bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
func Bf(planet1, planet2 string) []string {

	// Bf("Earth", "Mercury") ==> ("Venus")
	// Bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
	// Bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
	// Bf("Jupiter", "Saturn") ==> ("Uranus", "Neptune")
	// Bf("Saturn", "Neptune") ==> ("Uranus")
	// Bf("Uranus", "Neptune") ==> ()
	// Bf("Sun", "Moon") ==> ()
	// Bf("Moon", "Sun") ==> ()
	// Bf("Moon", "Mercury") ==> ("Earth", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
	// Bf("Mercury", "Moon") ==> ("Earth", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
	// Bf("Earth", "Moon") ==> ("Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
	// Bf("Mars", "Moon") ==> ("Jupiter", "Saturn", "Uranus", "Neptune")
	// Bf("Jupiter", "Moon") ==> ("Saturn", "Uranus", "Neptune")
	// Bf("Saturn", "Moon") ==> ("Uranus", "Neptune")
	// Bf("