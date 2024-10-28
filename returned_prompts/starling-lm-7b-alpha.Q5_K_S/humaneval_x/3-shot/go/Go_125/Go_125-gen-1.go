    result := make([]string, 0)
    for _, c := range txt {
        if c == ' ' || c == ',' {
            result = append(result, txt[:len(txt)-1])
            txt = txt[len(txt)-1:]
        } else if c >= 'a' && c <= 'z' {
            if (c - 'a') % 2 == 1 {
                result = append(result, string(c))
            }
        }
    }
    return result
}



