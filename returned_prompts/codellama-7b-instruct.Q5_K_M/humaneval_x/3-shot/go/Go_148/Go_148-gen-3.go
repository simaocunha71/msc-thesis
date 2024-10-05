    var result []string
    switch planet1 {
        case "Mercury":
            switch planet2 {
                case "Mercury":
                    result = []string{}
                case "Venus":
                    result = []string{"Venus"}
                case "Earth":
                    result = []string{"Venus", "Earth", "Mars"}
                case "Mars":
                    result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
                case "Jupiter":
                    result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"}
                case "Saturn":
                    result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
                case "Uranus":
                    result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
                case "Neptune":
                    result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
                default:
                    result = []string{}
            }
        case "Venus":
            switch planet2 {
                case "Venus":
                    result = []string{}
                case "Earth":
                    result = []string{"Venus", "Earth", "Mars"}
                case "Mars":
                    result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
                case "Jupiter":
                    result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"}
                case "Saturn":
                    result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}