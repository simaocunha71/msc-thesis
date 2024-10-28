    if len(arr) == 0 {
        return []int{}
    }

    smallest_even_value := math.MaxInt64
    smallest_even_index := -1

    for i, value := range arr {
        if value%2 == 0 && value < smallest_even_value {
            smallest_even_value = value
            smallest_even_index = i
        }
    }

    if smallest_even_index == -1 {
        return []int{}
    }

    return []int{smallest_even_value, smallest_even_index}
}



