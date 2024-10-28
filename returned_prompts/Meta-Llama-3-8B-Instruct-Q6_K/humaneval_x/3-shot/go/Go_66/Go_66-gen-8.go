    sum := 0
    for _, c := range x {
        if c > 64 && c < 91 {
            sum += int(c - 64)
        }
    }
    return sum
}
