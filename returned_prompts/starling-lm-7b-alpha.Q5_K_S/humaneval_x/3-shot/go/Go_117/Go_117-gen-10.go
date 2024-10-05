    result := make([]string, 0)
    word := ""
    consonants := "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for _, c := range s {
        if strings.Contains(consonants, string(c)) {
            word += string(c)
            if len(word) == n {
                result = append(result, word)
                word = ""
            }
        }else if c == ' ' {
            if len(word) == n {
                result = append(result, word)
                word = ""
            }else if len(word) > 0 && len(word) < n {
                result = append(result, word)
                word = ""
            }
        }else {
            word += string(c)
        }
    }
    if len(word) != 0 {
        result = append(result, word)
    }
    return result
}



