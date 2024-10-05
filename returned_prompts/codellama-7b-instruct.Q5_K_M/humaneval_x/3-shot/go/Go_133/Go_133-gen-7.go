    result := 0
    for _, v := range lst {
        result += int(math.Ceil(v)) * int(math.Ceil(v))
    }
    return result
}



