    vowels := []rune{'a', 'e', 'i', 'o', 'u'}
    result := 0
    for _, c := range s {
        if strings.ContainsRune(vowels, c) || (c == 'y' && strings.HasSuffix(s, string(c))){
            result++
        }
    }
    return result
}



