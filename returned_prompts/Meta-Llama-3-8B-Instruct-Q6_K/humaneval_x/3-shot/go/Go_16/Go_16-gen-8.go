    str = strings.ToLower(str)
    return len(strings.Map(func(r rune) rune {
        if strings.ContainsRune("abcdefghijklmnopqrstuvwxyz", r) {
            return r
        }
        return -1
    }, str))
}  // This function is not correct, because it counts the spaces as characters. It should not count them. The correct function is below

func CountDistinctCharacters(str string) int{
    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, char := range str {
        if char < 'a' || char > 'z' {
            continue
        }
        charSet[char] = true
    }
    return len(charSet)
}  // This function correctly counts the distinct characters in the string, ignoring spaces and case.  // This function correctly counts the distinct characters in the string, ignoring spaces and case.