    result := 0
    for _, e := range lst {
        result += int(math.Ceil(e) * math.Ceil(e))
    }
    return result
}



