    var min_value, index int
    for i, v := range arr {
        if v%2 == 0 && (min_value == 0 || v < min_value || v == min_value && i < index) {
            min_value = v
            index = i
        }
    }
    return []int{min_value, index}
}



