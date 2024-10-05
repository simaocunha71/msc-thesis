    vowels := "aeiouy"
    count := 0
    for _, r := range s {
        if strings.ContainsRune(vowels, r) {
            count += 1
        }
    }
    return count
}



