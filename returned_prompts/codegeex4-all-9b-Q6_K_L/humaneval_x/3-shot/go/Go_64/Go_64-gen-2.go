    vowels := "aeiou"
    s = strings.ToLower(s)
    count := 0
    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            count += 1
        }
    }
    if s[len(s)-1] == 'y' {
        count += 1
    }
    return count
}

