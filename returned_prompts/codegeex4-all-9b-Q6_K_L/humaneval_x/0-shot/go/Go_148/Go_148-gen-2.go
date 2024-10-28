func Bf(planet1, planet2 string) []string {
    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    var result []string
    for i := 0; i < len(planets); i++ {
        if planets[i] == planet1 || planets[i] == planet2 {
            for j := i + 1; j < len(planets); j++ {
                result = append(result, planets[j])
            }
            break
        }
    }
    return result
}

func main() {
    fmt.Println(Bf("Jupiter", "Neptune")) // ==> ("Saturn", "Uranus")
    fmt.Println(Bf("Earth", "Mercury"))   // ==> ("Venus")
    fmt.Println(Bf("Mercury", "Uranus"))  // ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
}
