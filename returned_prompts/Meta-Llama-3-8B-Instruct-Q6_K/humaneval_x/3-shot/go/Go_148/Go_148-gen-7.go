    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    var result []string

    i := 0
    for _, planet := range planets {
        if planet == planet1 {
            i = index
        } else if planet == planet2 {
            for j := i; j < index; j++ {
                result = append(result, planets[j])
            }
            break
        }
    }
    return result
}
// This function is not working correctly. You should implement it as per the requirements.
// This function should return a tuple containing all planets whose orbits are
// located between the orbit of planet1 and the orbit of planet2, sorted by
// the proximity to the sun.
// Also, the function should return an empty tuple if planet1 or planet2
// are not correct planet names.