    shift := 2 * 2
    result := ""

    for _, c := range s {
        if 'a' <= c && c <= 'z' {
            result += string((c-'a'+rune(shift))%26 + 'a')
        } else if 'A' <= c && c <= 'Z' {
            result += string((c-'A'+rune(shift))%26 + 'A')
        } else {
            result += string(c)
        }
    }

    return result
}



