    var result []string
    var buffer bytes.Buffer
    for _, c := range s {
        if c == ' ' {
            if buffer.Len() > 0 {
                word := buffer.String()
                if is_good(word, n) {
                    result = append(result, word)
                }
            }
            buffer.Reset()
        } else {
            is_vowel(c)
            buffer.WriteRune(c)
        }
    }
    return result
}

func is_vowel(r rune) {
    switch {
        case r >= 'a' && r <= 'z':
            if r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u':
                return
    }
}

func is_good(word string, n int) bool {
    var count int = 0
    for _, c := range word {
        if !is_vowel(c) {
            count += 1
        }
    }
    return count == n
}



