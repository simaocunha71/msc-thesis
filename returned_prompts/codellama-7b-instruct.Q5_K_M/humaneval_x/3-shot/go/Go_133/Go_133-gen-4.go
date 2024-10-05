    result := 0
    for _, n := range lst {
        result += int(math.Pow(math.Ceil(n), 2))
    }
    return result
}



