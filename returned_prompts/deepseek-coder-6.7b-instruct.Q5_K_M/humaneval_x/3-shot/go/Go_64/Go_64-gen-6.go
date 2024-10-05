    vowels := "aeiou"
    s = strings.ToLower(s)
    count := 0
    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            count++
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}



