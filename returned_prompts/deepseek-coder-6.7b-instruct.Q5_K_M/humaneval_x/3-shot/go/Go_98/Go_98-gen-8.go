    count := 0
    vowels := "AEIOU"
    for i := 0; i < len(s); i += 2 {
        if strings.ContainsRune(vowels, rune(s[i])) {
            count++
        }
    }
    return count
}



