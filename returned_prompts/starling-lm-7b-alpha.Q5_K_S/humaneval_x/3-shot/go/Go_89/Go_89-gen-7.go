    result := make([]rune, len(s))
    for i, c := range s {
        result[i] = c + 2*2 + (c/26)*26
    }
    return string(result)
}



