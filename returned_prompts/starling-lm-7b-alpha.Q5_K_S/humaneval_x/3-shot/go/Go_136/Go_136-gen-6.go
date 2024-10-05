    min_int := int(math.MaxInt32)
    max_int := int(math.MinInt32)

    for _, i := range lst {
        if i > max_int {
            max_int = i
        }
        if i < min_int {
            min_int = i
        }
    }

    return [2]interface{}{max_int, min_int}
}



