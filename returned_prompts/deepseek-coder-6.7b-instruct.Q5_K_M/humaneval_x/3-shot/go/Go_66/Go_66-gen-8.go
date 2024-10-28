    sum := 0
    for _, c := range x {
        if 'A' <= c && c <= 'Z' {
            sum += int(c)
        }
    }
    return sum
}



