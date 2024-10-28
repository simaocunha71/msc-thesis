    var last_consonant bool = false
    var vowel string = ""
    var last_char byte
    for i := len(word) - 1; i >= 0; i-- {
        char := word[i]
        if !last_consonant {
            last_consonant = true
        }

        if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' {
            vowel = string(char)
        }
        if char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' {
            last_char = char
        }
        if char != 'a' && char != 'e' && char != 'i' && char != 'o' && char != 'u' {
            last_consonant = false
        }
    }

    if vowel == "" {
        return vowel
    }
    if last_char == 'a' || last_char == 'e' || last_char == 'i' || last_char == 'o' || last_char == 'u' {
        return vowel
    }
    return ""
}



