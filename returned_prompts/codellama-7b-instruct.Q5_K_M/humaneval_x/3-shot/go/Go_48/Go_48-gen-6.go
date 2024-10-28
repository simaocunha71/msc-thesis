    var reverse_text []rune
    for _, c := range text {
        reverse_text = append(reverse_text, c)
    }
    for i := 0; i < len(text); i++ {
        if text[i] != reverse_text[len(reverse_text)-i-1]{
            return false
        }
    }
    return true
}



