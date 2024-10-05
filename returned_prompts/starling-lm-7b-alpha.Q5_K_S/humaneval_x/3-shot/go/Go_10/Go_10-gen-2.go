    palindrome_suffix := find_longest_palindrome_suffix(str)
    if len(palindrome_suffix) == 0 {
        return str
    }
    prefix := str[:len(str)-len(palindrome_suffix)]
    return prefix + palindrome_suffix + string(reverse(prefix))
}

func find_longest_palindrome_suffix(str string) string {
    if len(str) <= 1 {
        return str
    }
    result := ""
    for i := len(str) - 1; i >= 0; i-- {
        if strings.EqualFold(str[i:], str[:i]) {
            result = str[i:]
            break
        }
    }
    return result
}

func reverse(str string) []rune {
    result := make([]rune, 0)
    for _, r := range str {
        result = append(result, r)
    }
    i, j := 0, len(result) - 1
    for i < j {
        result[i], result[j] = result[j], result[i]
        i++
        j--
    }
    return result
}























































































































































































































