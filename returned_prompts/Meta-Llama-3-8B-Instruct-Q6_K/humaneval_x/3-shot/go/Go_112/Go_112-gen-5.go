    var result []byte
    for _, c := range s {
        if !strings.Contains(c, string(c)) {
            result = append(result, c)
        }
    }
    return [2]interface{}{string(result), isPalindrome(string(result))}
}

func isPalindrome(s string) bool {
    for i := 0; i < len(s)/2; i++ {
        if s[i] != s[len(s)-1-i] {
            return false
        }
    }
    return true
}