    var result string

    for x > 0 {
        var remainder int = x % base
        result = strconv.Itoa(remainder) + result
        x /= base
    }
    return result
}



