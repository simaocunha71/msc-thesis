    result := make([]string, 0)

    v := strings.Fields(s)
    for _, word := range v {
        n_consonants := 0
        for _, c := range word {
            if !is_vowel(c) {
                n_consonants += 1
            }
            if n_consonants > n {
                break
            }
        }
        if n_consonants == n {
            result = append(result, word)
        }
    }
    return result
}


func is_vowel(c byte) bool {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y'
}



