    for {
        var temp int
        temp = N
        for temp > 0 {
            temp = temp / 2
            if temp == 0 {
                break A
            }
        }
        N = N * 2
    }
    
    var binaryStr string
    var remainder int
    for N > 0 {
        remainder = N % 2
        N = N / 2
        binaryStr = strconv.Itoa(remainder) + binaryStr
    }
    return binaryStr
}
