    if IsPalindrome(str) {
        return str
    }

    longestPrefix := ""
    for i := 1; i < len(str); i++ {
        subStr := str[i:]
        if len(subStr) < len(str)/2 {
            continue
        }
        if IsPalindrome(subStr) {
            if len(longestPrefix) < len(subStr) {
                longestPrefix = subStr
            }
        }
    }

    return str + string(reversedSlices(longestPrefix)) + longestPrefix
}



