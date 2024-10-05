    result := make([]rune, 0)
    for _, c := range str {
        if c >= 'a' && c <= 'z'{
            result = append(result, rune(c - 32))
        }else if c >= 'A' && c <= 'Z'{
            result = append(result, rune(c + 32))
        }else {
            result = append(result, c)
        }
    }
    return string(result)
}



