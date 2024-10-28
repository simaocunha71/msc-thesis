    result := make([]string, 0)
    for _, s_char := range s {
        if !strings.ContainsRune(c, s_char) {
            result = append(result, string(s_char))
        }
    }
    return [2]interface{}{strings.Join(result, ""), IsPalindrome(strings.Join(result, ""))}
}



