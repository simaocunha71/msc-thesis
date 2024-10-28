    result := make([]rune, len(text))
    left := 0
    for i, c := range text {
        if c == ' ' {
            result[i] = '_'
        } else {
            result[i] = c
            left = i
        }
    }
    if left > 0 && left < len(text)-1 && text[left+1] == ' ' {
        result[left] = '-'
    }
    return string(result)
}



