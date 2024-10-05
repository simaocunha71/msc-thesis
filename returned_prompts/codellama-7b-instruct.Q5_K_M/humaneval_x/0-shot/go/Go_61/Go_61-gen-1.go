    // for every opening bracket, we need to find the corresponding closing bracket
    openingBrackets := strings.Split(brackets, "(")
    if len(openingBrackets) == 1 {
        return true
    }
    
    closingBrackets := strings.Split(brackets, ")")
    if len(closingBrackets) == 1 {
        return true
    }

    // if the number of opening brackets is not equal to the number of closing brackets,
    // then we know that the brackets are not correctly bracketed
    if len(openingBrackets) != len(closingBrackets) {
        return false
    }

    for i := 0; i < len(openingBrackets); i++ {
        if len(openingBrackets[i]) == 0 {
            continue
        }

        if len(closingBrackets[i]) == 0 {
            return false
        }
    }

    return true
}


