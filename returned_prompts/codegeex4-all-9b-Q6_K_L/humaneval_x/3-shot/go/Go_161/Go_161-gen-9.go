    result := make([]rune, 0)
    hasLetters := false
    for _, c := range s {
        if c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' {
            hasLetters = true
            if c >= 'a' && c <= 'z' {
                result = append(result, c - 'a' + 'A')
            } else {
                result = append(result, c - 'A' + 'a')
            }
        } else {
            result = append(result, c)
        }
    }
    if hasLetters {
        return string(result)
    } else {
        return Reverse(s)
    }
}

func Reverse(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}



