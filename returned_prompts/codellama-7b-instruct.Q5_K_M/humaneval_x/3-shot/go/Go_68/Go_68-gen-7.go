    var smallest_value, smallest_index int
    var even_values []int

    for i, v := range arr {
        if v%2 == 0 {
            even_values = append(even_values, v)

            if smallest_value == 0 || v < smallest_value {
                smallest_value = v
                smallest_index = i
            }
        }
    }

    if smallest_value == 0 {
        return []int{}
    } else {
        return []int{smallest_value, smallest_index}
    }
}



