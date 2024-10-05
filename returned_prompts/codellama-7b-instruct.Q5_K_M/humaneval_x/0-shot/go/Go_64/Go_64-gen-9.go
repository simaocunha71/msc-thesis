    for _, c := range s {
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
            continue
        }
        if c == 'y' {
            if strings.HasSuffix(s, "y") {
                continue
            }
        }
        return 0
    }
    return 1
}










