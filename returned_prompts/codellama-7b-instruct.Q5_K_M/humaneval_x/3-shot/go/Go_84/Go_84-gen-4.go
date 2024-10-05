    var result string = "0"
    for N > 0{
        var rem = N % 2
        result = strconv.Itoa(rem) + result
        N = N/2
    }
    return result
}



