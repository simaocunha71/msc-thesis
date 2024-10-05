    positives := make([]int, 0)
    for _, num := range l {
        if num > 0 {
            positives = append(positives, num)
        }
    }
    return positives
}



