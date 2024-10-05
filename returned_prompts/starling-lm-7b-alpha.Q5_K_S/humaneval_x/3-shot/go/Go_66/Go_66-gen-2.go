    result := 0
    for _, r := range x {
        if r >= 'A' && r <= 'Z' {
            result += int(r) - int('A') + 1
        }
    }
    return result
}




