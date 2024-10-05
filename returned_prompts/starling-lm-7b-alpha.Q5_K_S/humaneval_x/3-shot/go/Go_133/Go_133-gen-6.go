    var result int = 0
    for _, element := range lst {
        var rounded_element int = int(math.Ceil(element))
        result += rounded_element * rounded_element
    }
    return result
}



