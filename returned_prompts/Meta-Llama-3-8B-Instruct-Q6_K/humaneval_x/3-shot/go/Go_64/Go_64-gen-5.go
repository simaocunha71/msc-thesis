    s = strings.ToLower(s)
    count := 0
    for _, c := range s {
        switch c {
        case 'a', 'e', 'i', 'o', 'u', 'y':
            if c == 'y' && s[len(s)-1] == 'y' {
                continue
            }
            count++
        }
    }
    return count
} 