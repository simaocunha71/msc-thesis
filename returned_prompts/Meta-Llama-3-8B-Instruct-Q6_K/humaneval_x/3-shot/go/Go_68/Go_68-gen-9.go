    var result []int
    var min_even float64 = math.MaxFloat64
    var min_even_index int = -1

    for i, v := range arr {
        if v % 2 == 0 && v < min_even {
            min_even = float64(v)
            min_even_index = i
        }
    }

    if min_even != math.MaxFloat64 {
        result = []int(int(min_even), min_even_index)
    } else {
        result = []int{}
    }

    return result
}