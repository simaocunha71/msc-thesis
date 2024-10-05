    var ones int = 0
    for n > 0 {
        if n & 1 == 1 {
            ones += 1
        }
        n >>= 1
    }
    return ones
}



