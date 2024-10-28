    s = strings.ToLower(s)
    vowels := 0
    for _, c := range s {
        switch c {
        case 'a', 'e', 'i', 'o', 'u':
            vowels++
        }
    }
    if s[len(s)-1] == 'y' {
        vowels++
    }
    return vowels
}



