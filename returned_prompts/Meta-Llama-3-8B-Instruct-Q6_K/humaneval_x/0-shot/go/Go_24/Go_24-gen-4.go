    if n <= 0 {
        return 0
    }
    var divisor int
    for i := n - 1; i > 0; i-- {
        if n%i == 0 {
            divisor = i
            break
        }
    }
    return divisor
} // LargestDivisor


