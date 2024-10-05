    sum := 0
    for _, v := range x {
        if v >= 'A' && v <= 'Z' {
            sum += int(v)
        }
    }
    return sum
}



