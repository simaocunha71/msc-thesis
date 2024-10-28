    var min_even_value int
    var min_even_index int
    for i, v := range arr {
        if v % 2 == 0 {
            if min_even_value == 0 || v < min_even_value {
                min_even_value = v
                min_even_index = i
            }
        }
    }
    if min_even_value != 0 {
        return []int{min_even_value, min_even_index}
    } else {
        return []int{}
    }
}