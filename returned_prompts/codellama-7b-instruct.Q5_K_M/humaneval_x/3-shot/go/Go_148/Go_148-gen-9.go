    if planet1 == "Mercury" || planet2 == "Mercury"{
        return []string{"Venus"}
    }
    if planet1 == "Earth" || planet2 == "Earth"{
        return []string{"Venus", "Mars", "Jupiter", "Saturn"}
    }
    if planet1 == "Jupiter" || planet2 == "Jupiter"{
        return []string{"Saturn", "Uranus"}
    }
    return []string{}
}



