    result := make([]string, 0)
    words := strings.Fields(s)
    for _, word := range words {
        if countConsonants(word) == n {
            result = append(result, word)
        }
    }
    return result
}

func countConsonants(s string) int {
    consonants := "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count := 0
    for _, c := range s {
        if strings.ContainsRune(consonants, c) {
            count++
        }
    }
    return count
}



