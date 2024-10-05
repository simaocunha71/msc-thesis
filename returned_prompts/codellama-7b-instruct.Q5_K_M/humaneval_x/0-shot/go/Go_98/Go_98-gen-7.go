    for i, ch := range s {
        if i % 2 == 0 {
            if strings.ToUpper(string(ch)) != string(ch) {
                continue A
            }
        }
    }
    return 1
}
