    var unique_numbers = make([]int, 0)
    for _, number := range numbers {
        if !SliceContains(unique_numbers, number) {
            unique_numbers = append(unique_numbers, number)
        }
    }
    return unique_numbers
}



