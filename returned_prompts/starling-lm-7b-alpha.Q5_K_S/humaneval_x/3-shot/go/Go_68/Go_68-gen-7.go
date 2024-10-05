    result := make([]int, 0)

    for i, v := range arr {
        if v % 2 == 0 && (len(result) == 0 || result[0] > v) {
            result = append(result, v)
            result = append(result, i)
        }
    }
    return result
}



