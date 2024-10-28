    result := make([]rune, 0)
    for _, c := range message {
        if ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') {
            if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
                c += 2
                if c > 'z' {
                    c -= 26
                }
            }else{
                if c >= 'a' {
                    c += 1
                    if c > 'z' {
                        c -= 26
                    }
                }else if c >= 'A' {
                    c += 1
                    if c > 'Z' {
                        c -= 26
                    }
                }
            }
            result = append(result, c)
        }else{
            result = append(result, c)
        }
    }
    return string(result)
}



