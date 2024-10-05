    for i, b := range s {
        switch {
        case strings.ContainsRune("aeiou", b):
            continue A
        case b == 'y' && i == len(s)-1:
            continue A
        }
        break
    }
    return i
}
