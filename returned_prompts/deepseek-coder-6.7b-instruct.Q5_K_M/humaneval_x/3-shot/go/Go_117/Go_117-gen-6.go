    vowels := "aeiouAEIOU"
    words := strings.Fields(s)
    result := make([]string, 0)

    for _, word := range words {
        count := 0
        for _, letter := range word {
            if !strings.ContainsRune(vowels, letter) {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }

    return result
}



