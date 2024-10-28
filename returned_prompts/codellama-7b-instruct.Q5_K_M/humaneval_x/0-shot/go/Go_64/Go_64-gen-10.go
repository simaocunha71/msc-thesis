    for i, ch := range s {
        switch {
        case strings.ContainsRune("aeiouy", ch):
            continue A
        }
    }
    return 0
}

