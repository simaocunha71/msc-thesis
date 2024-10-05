    result := make([]rune, 0)
    for _, c1 := range s {
        if !strings.ContainsRune(c, c1) {
            result = append(result, c1)
        }
    }
    return [2]interface{}{string(result), IsPalindrome(string(result))}
}



