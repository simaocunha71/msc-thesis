
// There are eight planets in our solar system: the closest to the Sun
// is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn,
// Uranus, Neptune.
// Write a function that takes two planet names as strings planet1 and planet2.
// The function should return a tuple containing all planets whose orbits are
// located between the orbit of planet1 and the orbit of planet2, sorted by
// the proximity to the sun.
// The function should return an empty tuple if planet1 or planet2
// are not correct planet names.
// Examples
// Bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
// Bf("Earth", "Mercury") ==> ("Venus")
// Bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
func Bf(planet1, planet2 string) []string {

    var planets = []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var result []string

    switch {
    case planet1 == "Mercury":
        if planet2 == "Neptune":
            result = append(result, "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        else:
            result = append(result, "Venus", "Earth", "Mars", "Jupiter", "Saturn")
    case planet1 == "Venus":
        if planet2 == "Neptune":
            result = append(result, "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        else:
            result = append(result, "Earth", "Mars", "Jupiter", "Saturn")
    case planet1 == "Earth":
        if planet2 == "Neptune":
            result = append(result, "Mars", "Jupiter", "Sat