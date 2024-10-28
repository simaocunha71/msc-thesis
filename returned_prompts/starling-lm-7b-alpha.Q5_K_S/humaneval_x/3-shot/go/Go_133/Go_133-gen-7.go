    result := int(0)
    for _, elem := range lst {
        elem = math.Ceil(elem)
        result += int(math.Pow(elem, 2))
    }
    return result
}



