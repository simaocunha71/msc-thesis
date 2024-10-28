    var vowels = []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    var vowelMap = make(map[rune]bool)

    for _, v := range vowels {
        vowelMap[v] = true
    }

    for i := len(word) - 2; i > 0; i-- {
        if _, ok := vowelMap[rune(word[i+1])]; ok {
            continue
        }
        if _, ok := vowelMap[rune(word[i-1])]; ok {
            return string(rune(word[i]))
        }
    }
    return ""
}



