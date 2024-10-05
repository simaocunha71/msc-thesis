    result := make([]rune, len(s))

    for i, c := range s {
        result[i] = c + 2*2 + 'a'
    }
    return string(result)
}



