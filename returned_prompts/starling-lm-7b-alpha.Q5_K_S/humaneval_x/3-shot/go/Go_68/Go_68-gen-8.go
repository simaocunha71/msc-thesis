    result := []int{}
    for i, v := range arr {
        if v%2 == 0 && (len(result) == 0 || v < result[0]) {
            result = []int{v, i}
        }
    }
    return result
}



