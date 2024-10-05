    result := make([]int, 2)
    result[0] = math.MaxInt32
    result[1] = math.MaxInt32

    for i, v := range arr {
        if v % 2 == 0 && v < result[0] {
            result[0] = v
            result[1] = i
        }
    }

    return result
}



