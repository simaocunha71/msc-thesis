    if IsPalindrome(str) {
        return str
    }
    suffix := strings.Split(str, "")
    i := len(suffix) - 1
    for ; i >= 0; i-- {
        if IsPalindrome(strings.Join(suffix[i:], "")) {
            break
        }
    }
    prefix := strings.Split(str[:i], "")
    return strings.Join(append(prefix, reverseString(strings.Join(prefix[i:], ""))...), "")
}

func reverseString(s string) string {
    result := make([]byte, len(s))
    for i, c := range s {
        result[len(s)-i-1] = byte(c)
    }
    return string(result)
}



