    result := 0
    for _, element := range lst {
        rounded := int(math.Ceil(element))
        result += rounded * rounded
    }
    return result
}



