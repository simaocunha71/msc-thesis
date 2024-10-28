    vowels := "aeiouy"
    result := 0
    for _, c := range s {
        if strings.IndexRune(vowels, c) >= 0 {
            result += 1
        }
    }
    return result
}



