    var result []string
    s_runes := []rune(s)
    vowels := []rune{'a', 'e', 'i', 'o', 'u'}

    for i, r := range s_runes {
        if i == 0 || !isVowel(rune(s_runes[i-1])) {
            n--
        }
        if n == 0 && !isVowel(r) {
            result = append(result, s[i-len(s_runes)-1:i])
        }
    }
    return result
}

func isVowel(r rune) bool {
    for _, v := range vowels {
        if v == r {
            return true
        }
    }
    return false
}



