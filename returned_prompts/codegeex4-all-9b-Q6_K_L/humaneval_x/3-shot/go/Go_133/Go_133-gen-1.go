    result := 0
    for _, num := range lst {
        result += int(math.Pow(math.Ceil(num), 2))
    }
    return result
}

