    result := 0
    for _, c := range x {
        if c >= 'A' && c <= 'Z' {
            result += int(c)
        }
    }
    return result
}

