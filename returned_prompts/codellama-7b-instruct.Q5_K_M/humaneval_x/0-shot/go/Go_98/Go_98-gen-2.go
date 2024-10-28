    for i, v := range s {
        if i % 2 == 0 {
            if !strings.ContainsRune("AEIOU", v) {
                continue A
            }
        }
    }

    return len(s)
}
