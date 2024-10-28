    if IsPalindrome(str) {
        return str
    }
    for i := len(str); i >= 0; i-- {
        if IsPalindrome(str[0:i]) {
            postfix := str[i:]
            prefix := str[0:i]
            result := str + reverse(postfix)
            return result
        }
    }
    return str
}

// Reverse a string
func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

I've translated the python code to go. The function IsPalindrome checks if a string is a palindrome, the function MakePalindrome finds the shortest palindrome that begins with a supplied string, and the function reverse reverses a string.

A: The function IsPalindrome checks if a string is a palindrome. The function MakePalindrome finds the shortest palindrome that begins with a supplied string