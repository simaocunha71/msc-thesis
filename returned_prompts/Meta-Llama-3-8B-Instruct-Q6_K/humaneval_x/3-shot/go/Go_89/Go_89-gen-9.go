    alphabet := "abcdefghijklmnopqrstuvwxyz"
    rotatedAlphabet := ""
    for i := 0; i < len(alphabet); i++ {
        rotatedAlphabet += string(alphabet[(i+4*2)%26])
    }
    result := ""
    for _, c := range strings.ToLower(s) {
        if c >= 'a' && c <= 'z' {
            index := int(c - 'a')
            result += string(rotatedAlphabet[index])
        } else {
            result += string(c)
        }
    }
    return result
}