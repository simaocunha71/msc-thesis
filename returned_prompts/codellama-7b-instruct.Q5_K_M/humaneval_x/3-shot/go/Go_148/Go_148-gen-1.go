    switch planet1 {
    case "Mercury":
        switch planet2 {
        case "Neptune":
            return []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
        default:
            return []string{"Venus"}
        }
    case "Earth":
        switch planet2 {
        case "Mercury":
            return []string{"Venus"}
        default:
            return []string{}
        }
    case "Venus":
        switch planet2 {
        case "Earth":
            return []string{}
        default:
            return []string{"Venus"}
        }
    case "Mars":
        switch planet2 {
        case "Jupiter":
            return []string{"Saturn", "Uranus"}
        default:
            return []string{"Earth", "Mars"}
        }
    case "Jupiter":
        switch planet2 {
        case "Saturn":
            return []string{"Uranus"}
        default:
            return []string{"Earth", "Mars", "Jupiter"}
        }
    case "Saturn":
        switch planet2 {
        case "Uranus":
            return []string{}
        default:
            return []string{"Earth", "Mars", "Jupiter", "Saturn"}
        }
    case "Uranus":
        switch planet2 {
        case "Neptune":
            return []string{}
        default:
            return []string{"Saturn", "Uranus"}
        }
    case "Neptune":
        switch planet2 {
        case "Saturn":
            return []string{}
        default:
            return []string{}
        }
    default:
        return []string{}
    }
}



