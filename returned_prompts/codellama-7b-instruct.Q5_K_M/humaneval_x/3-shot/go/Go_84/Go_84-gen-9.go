    var result int
    var result_string string
    for N != 0 {
        result = N % 2
        result_string = strconv.Itoa(result) + result_string
        N = N / 2
    }
    return result_string
}



