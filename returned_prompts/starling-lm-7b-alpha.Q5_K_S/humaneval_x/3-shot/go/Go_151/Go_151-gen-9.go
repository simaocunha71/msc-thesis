    result := 0
    for _, element := range lst {
        if element > 0 && math.Floor(element) == element {
            result += int((element * element))
        }
    }
    return result
}



