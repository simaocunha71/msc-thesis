    var sum int
    for i, val := range lst {
        if i % 2 != 0 && val % 2 == 0 {
            sum += val
        }
    }
    return sum
}