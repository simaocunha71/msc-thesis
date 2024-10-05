    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    var result string
    for _, c := range word {
        if c >='a' && c <= 'z' {
            c += 'A' - 'a'
        }

        if c < 65 || c > 90 {
            continue
        }

        is_vowel := false
        for _, v := range vowels {
            if c == v {
                is_vowel = true
                result = string(c)
                break
            }
        }

        if is_vowel {
            break
        }
    }
    return result
}



