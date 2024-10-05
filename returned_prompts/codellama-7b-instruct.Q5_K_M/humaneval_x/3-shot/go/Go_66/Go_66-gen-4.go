    sum := 0
    for _, char := range x {
        if char >= 'A' && char <= 'Z' {
            sum += int(char)
        }
    }
    return sum
}



