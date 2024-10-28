    for i := 0; i < len(s); i++ {
        if i%2 == 0 {
            if strings.Contains(s[i], "A") {
                return 1
            }
        }
    }
    return 0
}


