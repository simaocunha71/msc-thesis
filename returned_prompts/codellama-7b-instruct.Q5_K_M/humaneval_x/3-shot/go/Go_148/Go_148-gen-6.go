    switch planet1 {
    case "Mercury":
        switch planet2 {
        case "Neptune":
            return []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
        case "Uranus":
            return []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
        }
    case "Earth":
        switch planet2 {
        case "Neptune":
            return []string{"Venus", "Mars", "Jupiter", "Saturn"}
        case "Uranus":
            return []string{"Venus", "Mars", "Jupiter", "Saturn"}
        }
    case "Jupiter":
        switch planet2 {
        case "Neptune":
            return []string{"Saturn", "Uranus"}
        case "Uranus":
            return []string{"Saturn"}
        }
    }
    return []string{}
}



