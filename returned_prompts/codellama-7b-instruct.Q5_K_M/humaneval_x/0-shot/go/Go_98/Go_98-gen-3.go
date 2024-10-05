    for i, c := range s {
        if i % 2 == 0 {
            if strings.ContainsRune("AEIOU", c) {
                continue A
            }
        }
    }

    return 0
}
