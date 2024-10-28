    positive_numbers  := make([]int, 0)
    for _, num := range l {
        if num > 0 {
            positive_numbers = append(positive_numbers, num)
        }
    }
    return positive_numbers
}



