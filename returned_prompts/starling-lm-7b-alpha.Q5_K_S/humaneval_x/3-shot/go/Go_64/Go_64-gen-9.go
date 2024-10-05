    vowels := "aeiouy"
    result := 0

    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            result += 1
        }
    }

    return result
}



