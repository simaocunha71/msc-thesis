    count := 0
    for i := 0; i < len(s); i++ {
        if i%2 == 0 {
            if strings.ContainsRune("AEIOU", rune(s[i])) {
                count++
            }
        }
    }
    return count
}


