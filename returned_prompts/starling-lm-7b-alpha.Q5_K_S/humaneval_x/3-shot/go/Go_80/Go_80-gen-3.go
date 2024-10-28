    if len(s) < 3 {
        return false
    }
    char_set := make(map[rune]bool)
    for i := 0; i < len(s)-2; i++ {
        if s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2] {
            return false
        }
        char_set[s[i]] = true
        char_set[s[i+1]] = true
        char_set[s[i+2]] = true
    }
    return true
}



