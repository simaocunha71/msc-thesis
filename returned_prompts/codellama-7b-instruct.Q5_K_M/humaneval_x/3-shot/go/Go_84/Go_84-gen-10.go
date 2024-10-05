    var result int

    for N > 0 {
        result += N % 2
        N /= 2
    }

    return strconv.Itoa(result)
}



