    positive := make([]int, 0)

    for _, num := range l {
        if num > 0 {
            positive = append(positive, num)
        }
    }

    return positive
}



