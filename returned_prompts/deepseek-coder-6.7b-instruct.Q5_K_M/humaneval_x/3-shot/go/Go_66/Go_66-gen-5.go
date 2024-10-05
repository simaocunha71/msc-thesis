    sum := 0
    for i := 0; i < len(x); i++ {
        if x[i] >= 'A' && x[i] <= 'Z' {
            sum += int(x[i])
        }
    }
    return sum
}



