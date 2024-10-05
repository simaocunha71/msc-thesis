    const vowels = "aeiou"
    const consonants = "bcdfghjklmnpqrstvwxyz"
    left := len(word) - 1
    for left > 0 {
        if vowels == "" {
            break
        }
        if consonants[0] == rune(word[left]) {
            for _, c := range consonants {
                if vowels[0] == rune(word[left-1]) {
                    left--
                    break
                } else if vowels[0] == c {
                    return string(c)
                }
            }
        }
        left--
    }
    return ""
}



