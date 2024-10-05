    s = strings.ToLower(s)
    count := 0
    for i := 0; i < len(s); i++ {
        if s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' {
            count++
        } else if i == len(s) - 1 && s[i] == 'y' {
            count++
        }
    }
    return count
}