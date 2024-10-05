    var sum int
    for _, c := range x {
        if 'A' <= c && c <= 'Z' {
            sum += int(c) - 'A' + 65
        }
    }
    return sum
}