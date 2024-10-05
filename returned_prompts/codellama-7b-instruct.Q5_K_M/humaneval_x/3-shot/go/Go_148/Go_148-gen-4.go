    var result []string

    if planet1 == "Mercury"{
        result = append(result, "Venus")
    }

    if planet1 == "Venus"{
        result = append(result, "Earth", "Mars", "Jupiter", "Saturn")
    }

    if planet1 == "Earth"{
        result = append(result, "Mars", "Jupiter", "Saturn")
    }

    if planet1 == "Mars"{
        result = append(result, "Jupiter", "Saturn")
    }

    if planet1 == "Jupiter"{
        result = append(result, "Saturn")
    }

    if planet1 == "Saturn"{
        result = append(result, "Uranus")
    }

    if planet1 == "Uranus"{
        result = append(result, "Neptune")
    }

    return result
}



