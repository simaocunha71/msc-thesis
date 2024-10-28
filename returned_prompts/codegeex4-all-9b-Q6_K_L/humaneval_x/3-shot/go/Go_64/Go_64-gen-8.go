    vowels := "aeiouAEIOU"
    count := 0
    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            count++
        }
    }
    return count
}

