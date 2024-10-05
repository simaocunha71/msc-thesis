    var r = 1
    for i := 0; i < 31; i++ {
        r <<= 1
        if r >= p {
            r %= p
        }
        if (n&(1<<i)) != 0 {
            r *= 2
            if r >= p {
                r %= p
            }
        }
    }
    return r
}



