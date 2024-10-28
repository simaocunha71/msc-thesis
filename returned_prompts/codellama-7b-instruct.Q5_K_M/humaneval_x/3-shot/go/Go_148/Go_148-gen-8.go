    var result []string
    switch planet1 {
    case "Mercury":
        switch planet2 {
        case "Neptune":
            result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
        case "Uranus":
            result = []string{"Venus", "Earth", "Mars"}
        }
    case "Earth":
        switch planet2 {
        case "Neptune":
            result = []string{"Venus", "Mars", "Jupiter", "Saturn"}
        case "Uranus":
            result = []string{"Venus", "Mars"}
        }
    case "Jupiter":
        switch planet2 {
        case "Neptune":
            result = []string{"Saturn", "Uranus"}
        case "Uranus":
            result = []string{"Saturn"}
        }
    case "Saturn":
        switch planet2 {
        case "Neptune":
            result = []string{}
        case "Uranus":
            result = []string{}
        }
    }
    return result
}



