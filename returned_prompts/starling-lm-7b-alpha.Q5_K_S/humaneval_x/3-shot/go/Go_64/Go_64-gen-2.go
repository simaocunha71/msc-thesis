    vowels := "aeiouy"
    count := 0
    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            count += 1
        }
    }
    return count
}



