    for i  := 0; i < len(text)/2; i++ {
        if text[i] != text[len(text)-i-1] {
            return false
        }
    }
    return true
}



