    result := 0
    vowels := "aeiouy"
    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            result++
        }
    }
    return result
}



