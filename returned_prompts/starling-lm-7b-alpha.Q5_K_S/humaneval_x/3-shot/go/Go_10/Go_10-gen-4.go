    if IsPalindrome(str) {
        return str
    }
    var max_palindrome_length int
    var max_palindrome_end int
    for i := len(str) - 1; i >= 0; i-- {
        prefix := str[:i]
        suffix := str[i:]
        if is_palindrome(suffix) {
            if max_palindrome_length < len(suffix) {
                max_palindrome_length = len(suffix)
                max_palindrome_end = i
            }
        }
    }
    prefix := str[:max_palindrome_end]
    suffix := str[max_palindrome_end:]
    return prefix + reverse(suffix) + prefix[len(prefix)-len(suffix):]
}

func is_palindrome(str string) bool {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return str == string(result)
}

func reverse(str string) string {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result)
}



