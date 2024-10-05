    if IsPalindrome(str) {
        return str
    }

    // Find the longest postfix of str that is a palindrome.
    var palindromic_suffix string
    for i := len(str); i > 0; i-- {
        if IsPalindrome(str[len(str)-i:]) {
            palindromic_suffix = str[len(str)-i:]
            break
        }
    }

    // Find the prefix that comes before the palindromic suffix.
    prefix := str[:len(str)-len(palindromic_suffix)]

    // Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return prefix + Reverse(palindromic_suffix)
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



