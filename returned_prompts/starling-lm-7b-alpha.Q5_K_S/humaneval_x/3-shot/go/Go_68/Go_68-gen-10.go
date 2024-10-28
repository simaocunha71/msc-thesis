    result := make([]int, 0)
    min := math.MaxInt64
    for i, v := range arr {
        if v%2 == 0 && v < min {
            min = v
            result = []int{v, i}
        }
    }
    return result
}



