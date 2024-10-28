    positive_numbers := make([]int, 0)
    for _, number := range l {
        if number > 0 {
            positive_numbers = append(positive_numbers, number)
        }
    }
    return positive_numbers
}



