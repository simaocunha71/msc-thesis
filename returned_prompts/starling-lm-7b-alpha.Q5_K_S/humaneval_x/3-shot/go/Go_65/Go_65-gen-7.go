    var result []rune = make([]rune, 0)
    var n = int(math.Log10(float64(x))) + 1

    for i := 0; i < n; i++ {
        var digit = x % 10
        result = append(result, rune(digit + '0'))
        x /= 10
    }

    for i := shift; i < n; i++ {
        result = append(result[:1], result[i:]...)
    }
    return string(result)
}



