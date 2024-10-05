    var left, right rune
    var left_found, right_found bool
    var current_vowel rune
    var result string
    var vowels = []rune{'a', 'e', 'i', 'o', 'u'}

    for i := 0; i < len(word); i++ {
        current_vowel = word[i]
        if current_vowel == 'a' || current_vowel == 'e' || current_vowel == 'i' || current_vowel == 'o' || current_vowel == 'u' {
            if !left_found {
                left_found = true
                left = current_vowel
            }
            if !right_found {
                right_found = true
                right = current_vowel
            }
        }
        if left_found && right_found {
            break
        }
    }
    for i := 0; i < len(word); i++ {
        current_vowel = word[len(word)-i-1]
        if current_vowel == 'a' || current_vowel == 'e' || current_vowel == 'i' || current_vowel == 'o' || current_vowel == 'u' {
            if !right_found {
                right_found = true
                right = current_vowel
            }
            if !left_found {
                left_found = true
                left = current_vowel
            }
        }
        if left_found && right_found {
            break
        }
    }
    for _, vowel := range vowels {
        if vowel == left && vowel == right {
            return string(vowel)
        }
    }
    if left_found && right_found {
        return string(left)
    }
    return ""
}



