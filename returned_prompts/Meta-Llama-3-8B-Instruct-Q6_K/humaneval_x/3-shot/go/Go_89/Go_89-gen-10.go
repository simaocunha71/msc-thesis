    alphabet := "abcdefghijklmnopqrstuvwxyz"
    result := ""
    for _, c := range strings.ToLower(s) {
        if c >= 'a' && c <= 'z' {
            index := int(c - 'a')
            result += string(alphabet[(index+2*2)%26])
        } else {
            result += string(c)
        }
    }
    return result
}