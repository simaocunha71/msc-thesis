    if len(str) == 0 {
        return ""
    }
    longest_palindromic_suffix := longestPalindromicSuffix(str)
    if len(longest_palindromic_suffix) == len(str) {
        return str + longest_palindromic_suffix
    }
    prefix := str[:len(str) - len(longest_palindromic_suffix)]
    return prefix + string(reverse(longest_palindromic_suffix)) + prefix[ :len(prefix) - 1]
}

func longestPalindromicSuffix(s string) string {
    if len(s) == 0 {
        return ""
    }
    i := 0
    j := len(s) - 1
    for i < j {
        if s[i] != s[j] {
            break
        }
        i++
        j--
    }
    if i == j {
        return s[i: j + 1]
    }
    return ""
}

func reverse(s string) string {
    result := make([]rune, 0, len(s))
    for _, c := range s {
        result = append(result, c)
    }
    for i, j := 0, len(result) - 1; i < j; i, j = i + 1, j - 1 {
        result[i], result[j] = result[j], result[i]
    }
    return string(result)
}



