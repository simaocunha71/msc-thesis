    min_even := math.MaxInt64
    min_even_index := -1

    for i, v := range arr {
        if v % 2 == 0 && v < min_even {
            min_even = v
            min_even_index = i
        }
    }

    if min_even_index == -1 {
        return []int{}
    }

    return []int{min_even, min_even_index}
}