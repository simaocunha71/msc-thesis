    for i := 0; i < len(s); i++ {
        if i % 2 == 0 && strings.Index(s[i], "A") != -1 {
            goto A
        }
    }
}


