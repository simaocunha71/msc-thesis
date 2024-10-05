    result := 0
    for _, c := range x {
        if c >= 'A' && c <= 'Z' {
            result += int(c) - int('A') + 1
        }
    }
    return result
}




