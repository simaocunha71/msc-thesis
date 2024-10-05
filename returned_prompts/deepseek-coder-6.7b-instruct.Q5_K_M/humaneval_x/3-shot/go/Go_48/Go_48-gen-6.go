    length  := len(text)
    for i:= 0; i < length/2; i++ {
        if text[i] != text[length-i-1] {
            return false
        }
    }
    return true
}



