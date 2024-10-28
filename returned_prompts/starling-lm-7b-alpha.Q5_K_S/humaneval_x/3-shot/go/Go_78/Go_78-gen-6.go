    result := 0
    for _, r := range num {
        switch {
        case r == '2':
            result += 1
        case r == '3':
            result += 1
        case r == '5':
            result += 1
        case r == '7':
            result += 1
        case r >= 'A' && r <= 'F':
            result += 1
        }
    }
    return result
}



