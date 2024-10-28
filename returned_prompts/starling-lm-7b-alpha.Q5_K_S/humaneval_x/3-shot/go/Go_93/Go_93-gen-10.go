    result := make([]rune, 0)
    for _, c := range message {
        if strings.IndexRune("aeiou", c) != -1 {
            result = append(result, ' '+string(rune(c+2))+' ')
        }else if strings.IndexRune("AEIOU", c) != -1 {
            result = append(result, ' '+string(rune(c-2))+' ')
        }else {
            result = append(result, c)
        }
    }
    return string(result)
}



