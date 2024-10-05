    vowels := []rune{'a','e','i','o','u','A','E','I','O','U'}
    result := ""
    for i := 2; i < len(word); i++ {
        if !bytes.Contains(vowels, []rune{word[i]} ) {
            continue
        }
        if result == "" {
            result = string(word[i])
        }else if word[i] != word[i-1] && word[i] != word[i+1] {
            result = string(word[i])
        }
    }
    return result
}



