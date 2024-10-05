    result := strings.Map(func(r rune) rune {
        if strings.IndexRune(c, r) != -1 {
            return -1
        }
        return r
    }, s)

    return [2]interface{}{string(result), isPalindrome(result)}
}

func isPalindrome(s string) bool {
    for i, c := range s {
        if i == len(s)-i-1 {
            return c == rune(c)
        }
    }
    return true
}



