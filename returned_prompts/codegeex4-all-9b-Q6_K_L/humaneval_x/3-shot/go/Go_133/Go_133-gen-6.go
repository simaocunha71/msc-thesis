    result := 0
    for _, elem := range lst{
        result += int(math.Pow(math.Ceil(elem),2))
    }
    return result
}



