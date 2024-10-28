    result := 0
    for _, char := range x {
        if char >= 'A' && char <= 'Z' {
            result += int(char) - int('A') + 1
        }
    }
    return result
}



