    result := ""
    if !IsPalindrome(str) {
        // Find the longest palindromic suffix
        suffix := ""
        for i := len(str) - 1; i >= 0; i-- {
            suffix = str[i:]
            if IsPalindrome(suffix) {
                break
            }
        }
        // Construct the shortest palindrome
        result = str + strings.Split(str[:len(str)-len(suffix)], "")[0] + strings.Split(suffix, "")[1:][0][:len(suffix):len(suffix)]
    }else{
        result = str
    }
    return result
}



