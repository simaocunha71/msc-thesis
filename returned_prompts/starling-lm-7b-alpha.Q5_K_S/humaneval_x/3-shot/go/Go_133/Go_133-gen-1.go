    result := int(0)
    for _, v := range lst {
        v_int := math.Ceil(v)
        result += int(math.Pow(v_int, 2))
    }
    return result
}



