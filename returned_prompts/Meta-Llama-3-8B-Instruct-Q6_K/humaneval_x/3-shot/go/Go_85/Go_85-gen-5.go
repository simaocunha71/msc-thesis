    var sum int
    for i, x := range lst {
        if i % 2 != 0 && x % 2 == 0 {
            sum += x
        }
    }
    return sum
}