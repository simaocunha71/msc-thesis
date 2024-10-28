    result := ""
    for i := len(str) - 1; i >= 0; i-- {
        suffix := str[i:]
        if IsPalindrome(suffix) && len(suffix) > len(result) {
            result = suffix
        }
    }
    return result
}



