    planets := []string{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    planet_map := map[string]int{
        "Mercury": 0,
        "Venus": 1,
        "Earth": 2,
        "Mars": 3,
        "Jupiter": 4,
        "Saturn": 5,
        "Uranus": 6,
        "Neptune": 7,
    }
    i, j := planet_map[planet1], planet_map[planet2]
    if i < 0 || j < 0 || i >= len(planets) || j >= len(planets) {
        return []string{}
    }
    result := make([]string, 0)
    for k := i + 1; k < j; k++ {
        result = append(result, planets[k])
    }
    return result
}