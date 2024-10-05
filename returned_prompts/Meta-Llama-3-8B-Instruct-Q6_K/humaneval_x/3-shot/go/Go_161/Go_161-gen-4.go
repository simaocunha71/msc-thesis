    result := make([]byte, 0)

    for _, c := range s {
        if 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' {
            if c >= 'a' && c <= 'z' {
                result = append(result, byte(c - 32))
            } else {
                result = append(result, byte(c + 32))
            }
        } else {
            result = append(result, c)
        }
    }

    if len(result) == 0 {
        return string([]byte{'\0'})
    } else {
        return string(Reverse(result))
    }
}

func Reverse(s []byte) []byte {
    r := []byte{}
    for i := len(s) - 1; i >= 0; i-- {
        r = append(r, s[i])
    }
    return r
}