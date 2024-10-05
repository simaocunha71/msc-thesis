    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for i, c := range word {
        if !bytes.IndexRune(vowels, c) == -1 {
            if i != 0 && i != len(word) - 1 {
                return string(c)
            }
        }
    }
    return ""
}



