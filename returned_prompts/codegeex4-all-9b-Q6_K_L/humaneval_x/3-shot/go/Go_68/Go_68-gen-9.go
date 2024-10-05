    result := make([]int, 0)
    for i, v := range arr {
        if v % 2 == 0 {
            if len(result) == 0 {
                result = append(result, v)
                result = append(result, i)
            }else if v < result[0] {
                result[0] = v
                result[1] = i
            }
        }
    }
    return result
}



