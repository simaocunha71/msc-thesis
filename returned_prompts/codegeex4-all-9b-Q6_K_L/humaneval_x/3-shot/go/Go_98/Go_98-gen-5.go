    count := 0
    vowels := "AEIOU"
    for i, c := range s {
        if i % 2 == 0 {
            if strings.ContainsRune(vowels, c) {
                count += 1
            }
        }
    }
    return count
}



