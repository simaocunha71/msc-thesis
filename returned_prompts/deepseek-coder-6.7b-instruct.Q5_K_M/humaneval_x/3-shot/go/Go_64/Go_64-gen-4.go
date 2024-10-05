    s = strings.ToLower(s)
    count := 0
    for _, c := range s {
        switch c {
        case 'a', 'e', 'i', 'o', 'u':
            count++
        }
    }
    if s[len(s)-1] == 'y' {
        count++
    }
    return count
}



