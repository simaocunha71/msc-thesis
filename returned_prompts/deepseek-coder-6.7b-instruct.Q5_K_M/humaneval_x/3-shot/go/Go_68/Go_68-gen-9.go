    smallest_even_value, smallest_even_index := math.MaxInt64, -1

    for index, value := range arr {
        if value % 2 == 0 && value <= smallest_even_value {
            smallest_even_value = value
            smallest_even_index = index
        }
    }

    if smallest_even_index == -1 {
        return []int{}
    }

    return []int{smallest_even_value, smallest_even_index}
}



