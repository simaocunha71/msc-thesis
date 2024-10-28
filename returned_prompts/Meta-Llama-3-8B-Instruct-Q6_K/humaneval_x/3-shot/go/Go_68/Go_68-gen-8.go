    var min_even int
    var min_even_index int
    var min_even_found bool

    for i, v := range arr {
        if v % 2 == 0 {
            if !min_even_found || v < min_even {
                min_even = v
                min_even_index = i
                min_even_found = true
            }
        }
    }

    if min_even_found {
        return []int{min_even, min_even_index}
    } else {
        return []int{}
    }
}