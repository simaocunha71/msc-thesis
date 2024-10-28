    var result string
    for N > 0 {
        result = strconv.Itoa(N % 2) + result
        N /= 2
    }
    return result
}



