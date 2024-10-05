    var result string
    for N > 0 {
        remainder := N % 2
        N = N / 2
        result = strconv.Itoa(int(remainder)) + result
    }
    return result
}  // Convert to binary and return the binary string.