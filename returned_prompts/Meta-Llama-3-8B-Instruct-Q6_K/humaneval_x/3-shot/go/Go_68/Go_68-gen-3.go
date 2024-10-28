    var result []int
    var min_even int = math.MaxInt64
    var min_index int = -1

    for i, val := range arr {
        if val % 2 == 0 && val < min_even {
            min_even = val
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