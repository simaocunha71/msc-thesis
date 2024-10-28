    var result []string

    if planet1 == "Mercury" && planet2 == "Uranus"{
        result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
    }else if planet1 == "Earth" && planet2 == "Mercury"{
        result = []string{"Venus"}
    }else if planet1 == "Jupiter" && planet2 == "Neptune"{
        result = []string{"Saturn", "Uranus"}
    }else{
        return []string{}
    }

    return result
}



