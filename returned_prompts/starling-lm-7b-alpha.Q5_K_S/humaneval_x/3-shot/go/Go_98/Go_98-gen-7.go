    result := 0
    for i := 0; i < len(s); i++ {
        if i % 2 == 0 {
            if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') {
                result++
            }
        }
    }
    return result
}



