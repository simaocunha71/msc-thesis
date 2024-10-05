    var sum int
    for _, c := range x {
        if c >= 'A' && c <= 'Z' {
            sum += int(c)
        }else if c >= 'a' && c <= 'z' {
            sum += int(c)
        }
    }
    return sum
}



