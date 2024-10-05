    result := make([]rune, 0)
    for _, r := range s {
        if !strings.ContainsRune(c,r) {
            result = append(result, r)
        }
    }
    return [2]interface{}{string(result), isPalindrome(string(result))}
}

// Check if a string is palindrome or not
func isPalindrome(s string) bool {
    return s == strings.Reverse(s)
}



