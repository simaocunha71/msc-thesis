    result := make([]rune, 0)
    for _, c := range message {
        if (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
            if c == 'a' || c == 'A' {
                result = append(result, 'c')
            }else if c == 'e' || c == 'E' {
                result = append(result, 'g')
            }else if c == 'i' || c == 'I' {
                result = append(result, 'k')
            }else if c == 'o' || c == 'O' {
                result = append(result, 'u')
            }else if c == 'u' || c == 'U' {
                result = append(result, 'w')
            }else if c == ' ' {
                result = append(result, ' ')
            }else {
                if c >= 'A' && c <= 'Z' {
                    result = append(result, c-'A'+'a')
                }else {
                    result = append(result, c-'a'+'A')
                }
            }
        }
    }
    return string(result)
}



