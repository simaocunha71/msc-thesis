    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowelMap := make(map[rune]bool)
    for _, v := range vowels {
        vowelMap[v] = true
    }

    for i := len(word) - 2; i > 0; i-- {
        if _, ok := vowelMap[rune(word[i])]; ok {
            continue
        }
        for _, v := range vowels {
            if rune(word[i-1]) != v && rune(word[i+1]) != v {
                return string(v)
            }
        }
    }
    return ""
}



