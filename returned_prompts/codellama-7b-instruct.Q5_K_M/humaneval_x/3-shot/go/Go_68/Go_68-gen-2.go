    smallest_value := math.MaxInt32
    smallest_index := -1

    for i, n := range arr {
        if n%2 == 0 && n < smallest_value {
            smallest_value = n
            smallest_index = i
        }
    }
    return []int{smallest_value, smallest_index}
}



