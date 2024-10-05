    var sum int
    for i, v := range lst {
        if i%2 != 0 && v%2 == 0 {
            sum += v
        }
    }
    return sum
}