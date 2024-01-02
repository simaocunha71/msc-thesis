
// There are eight planets in our solar system: the closerst to the Sun
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
    var list []string
    if !IsPlanetName(planet1, false) || !IsPlanetName(planet2, false) { return list }
    var listOfAll = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}

    for _, p := range listOfAll {
        if IsIn(p, planet1, planet2, false) {
            if !IsPlanetName(planet1, true) || !IsPlanetName(planet2, true) { return nil }
            list = append(list, p)
        }
    }
    return list
}