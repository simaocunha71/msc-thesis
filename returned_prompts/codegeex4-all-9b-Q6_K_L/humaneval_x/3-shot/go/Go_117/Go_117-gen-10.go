    result := make([]string, 0)
    vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
    words := strings.Fields(s)
    for _, word := range words {
        count := 0
        for _, c := range word {
            if !vowels[c] {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}



