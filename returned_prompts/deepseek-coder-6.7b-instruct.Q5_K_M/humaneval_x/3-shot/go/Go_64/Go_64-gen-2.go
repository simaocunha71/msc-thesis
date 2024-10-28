    s = strings.ToLower(s)
    count := 0
    for _, c := range s {
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
            count++
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}



