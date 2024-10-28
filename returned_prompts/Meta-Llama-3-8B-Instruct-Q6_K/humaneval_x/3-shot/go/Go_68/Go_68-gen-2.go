    var result []int
    min_even := math.MaxInt64
    min_index := -1

    for i, v := range arr {
        if v % 2 == 0 && v < min_even {
            min_even = v
            min_index = i
        }
    }

    if min_even != math.MaxInt64 {
        result = []int{min_even, min_index}
    } else {
        result = []int{}
    }

    return result
}