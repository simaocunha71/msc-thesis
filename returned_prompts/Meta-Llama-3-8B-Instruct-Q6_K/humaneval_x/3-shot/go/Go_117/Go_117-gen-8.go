    words := strings.Split(s, " ")
    result := make([]string, 0)
    for _, word := range words {
        if len(word) > n {
            word = word[:n]
        }
        if countConsonants(word) == n {
            result = append(result, word)
        }
    }
    return result
}

func countConsonants(word string) int {
    count := 0
    for _, char := range word {
        if !isVowel(char) {
            count++
        }
    }
    return count
}

func isVowel(char rune) bool {
    vowels := []rune("aeiouAEIOU")
    for _, v := range vowels {
        if char == v {
            return true
        }
    }
    return false
}
}  // Don't forget the final closing brace!