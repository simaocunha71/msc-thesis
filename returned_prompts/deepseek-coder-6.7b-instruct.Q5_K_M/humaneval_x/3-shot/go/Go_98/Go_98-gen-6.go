    vowels := "AEIOU"
    count := 0

    for i := 0; i < len(s); i += 2 {
        if strings.ContainsRune(vowels, rune(s[i])) {
            count++
        }
    }

    return count
}



