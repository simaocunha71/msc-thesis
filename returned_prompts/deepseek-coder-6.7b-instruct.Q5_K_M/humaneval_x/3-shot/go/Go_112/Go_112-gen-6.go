    for _, ch := range c {
        s = strings.ReplaceAll(s, string(ch), "")
    }
    
    return [2]interface{}{s, isPalindrome(s)}
}

func isPalindrome(s string) bool {
    for i := 0; i < len(s)/2; i++ {
        if s[i] != s[len(s)-i-1] {
            return false
        }
    }
    return true
}



