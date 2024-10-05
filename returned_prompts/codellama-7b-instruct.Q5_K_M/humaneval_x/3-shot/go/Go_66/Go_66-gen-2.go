    sum := 0
    for _, c := range x {
        if c >= 'A' && c <= 'Z' {
            sum += int(c)
        }
    }
    return sum
}



