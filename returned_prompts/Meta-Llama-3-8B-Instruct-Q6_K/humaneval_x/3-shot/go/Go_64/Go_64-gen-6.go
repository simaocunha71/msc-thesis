    count := 0
    s = strings.ToLower(s)
    for i := 0; i < len(s); i++ {
        if s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' {
            count++
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}