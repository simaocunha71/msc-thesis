    vowels := "aeiouy"
    counter := 0
    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            counter++
        }
    }
    return counter
}



