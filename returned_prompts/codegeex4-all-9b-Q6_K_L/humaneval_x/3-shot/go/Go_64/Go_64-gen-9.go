    s = strings.ToLower(s)
    count := 0
    if strings.HasSuffix(s, "y") {
        count++
    }
    for _, c := range s {
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
            count++
        }
    }
    return count
}

