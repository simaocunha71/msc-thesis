    if planet1 != "Mercury" && planet2 != "Neptune"{
        return []string{}
    }

    var result []string

    if planet1 == "Mercury"{
        result = []string{"Venus"}
    }
    if planet1 == "Earth"{
        result = []string{"Venus", "Mars", "Jupiter", "Saturn"}
    }
    if planet1 == "Mars"{
        result = []string{"Venus", "Earth", "Jupiter", "Saturn"}
    }
    if planet1 == "Jupiter"{
        result = []string{"Venus", "Earth", "Mars", "Saturn"}
    }
    if planet1 == "Saturn"{
        result = []string{"Venus", "Earth", "Mars", "Jupiter"}
    }
    if planet1 == "Uranus"{
        result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
    }
    if planet1 == "Neptune"{
        result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"}
    }

    return result
}



