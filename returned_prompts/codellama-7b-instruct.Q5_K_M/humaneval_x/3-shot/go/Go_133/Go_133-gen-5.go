    result := 0
    for _, v := range lst {
        result += int(math.Pow(math.Ceil(v), 2))
    }
    return result
}



