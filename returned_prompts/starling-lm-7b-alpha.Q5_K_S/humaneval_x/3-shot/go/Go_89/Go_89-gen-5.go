    result := make([]rune, len(s))

    for i, c := range s {
        result[i] = c + (c-'a'-2)%26 + 'a'
    }
    return string(result)
}



