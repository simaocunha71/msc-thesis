    var sum int
    for _, c := range x {
        if c >= 'A' && c <= 'Z' {
            sum += int(c - 'A' + 65)
        }
    }
    return sum
}