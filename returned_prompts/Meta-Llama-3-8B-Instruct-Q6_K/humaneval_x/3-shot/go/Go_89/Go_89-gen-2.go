    alphabet := "abcdefghijklmnopqrstuvwxyz"
    shiftedAlphabet := strings.Repeat(alphabet, 2)
    result := ""
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            index := int(c - 'a')
            result += string(shiftedAlphabet[index:index+1])
        } else {
            result += string(c)
        }
    }
    return result
}