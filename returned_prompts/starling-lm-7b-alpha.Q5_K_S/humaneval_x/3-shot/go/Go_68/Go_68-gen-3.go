    result := make([]int, 0)
    smallest_even_value := math.MaxInt32
    smallest_even_index := -1
    for i, v := range arr {
        if v%2 == 0 && v < smallest_even_value {
            smallest_even_value = v
            smallest_even_index = i
        }
    }
    if smallest_even_index != -1 {
        result = append(result, smallest_even_value, smallest_even_index)
    }
    return result
}



