    var result []string

    if planet1 == "Mercury"{
        if planet2 == "Neptune"{
            result = []string{"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
        }else{
            result = []string{"Venus"}
        }
    }else if planet1 == "Earth"{
        if planet2 == "Neptune"{
            result = []string{"Mars", "Jupiter", "Saturn"}
        }else{
            result = []string{}
        }
    }else if planet1 == "Venus"{
        if planet2 == "Neptune"{
            result = []string{"Mars", "Jupiter", "Saturn"}
        }else{
            result = []string{"Mars"}
        }
    }else if planet1 == "Mars"{
        if planet2 == "Neptune"{
            result = []string{"Jupiter", "Saturn"}
        }else{
            result = []string{}
        }
    }else if planet1 == "Jupiter"{
        if planet2 == "Neptune"{
            result = []string{"Saturn"}
        }else{
            result = []string{}
        }
    }else if planet1 == "Saturn"{
        if planet2 == "Neptune"{
            result = []string{}
        }else{
            result = []string{}
        }
    }else if planet1 == "Uranus"{
        if planet2 == "Neptune"{
            result = []string{}
        }else{
            result = []string{}
        }
    }else if planet1 == "Neptune"{
        if planet2 == "Neptune"{
            result = []string{}
        }else{
            result = []string{}
        }
    }else{
        result = []string{}
    }

    return result
}



