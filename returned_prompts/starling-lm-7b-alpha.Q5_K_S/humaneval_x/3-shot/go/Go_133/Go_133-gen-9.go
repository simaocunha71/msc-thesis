    result := int(0)
    for _, v := range lst {
        result += int(math.Ceil(v) * math.Ceil(v))
    }
    return result
}



