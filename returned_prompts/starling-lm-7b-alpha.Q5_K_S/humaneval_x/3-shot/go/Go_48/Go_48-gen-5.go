    for i, v := range text {
        if text[len(text)-i-1] != v {
            return false
        }
    }
    return true
}



