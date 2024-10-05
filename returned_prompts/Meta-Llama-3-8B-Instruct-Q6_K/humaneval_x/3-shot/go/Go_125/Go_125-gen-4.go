    words := strings.Split(txt, " ")
    if len(words) > 0 {
        return words
    }
    words = strings.Split(txt, ",")
    if len(words) > 0 {
        return words
    }
    var count int
    for i := 0; i < len(txt); i++ {
        if 'a' <= txt[i] && txt[i] <= 'z' {
            if (int(txt[i]) - int('a')) % 2 != 0 {
                count++
            }
        }
    }
    return count
} 





