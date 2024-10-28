    words := strings.Split(txt, " ")
    if len(words) == 1 {
        words = strings.Split(txt, ",")
    }
    if len(words) == 1 {
        count := 0
        for i := 0; i < len(txt); i++ {
            if i % 2 != 0 && txt[i] >= 'a' && txt[i] <= 'z' {
                count++
            }
        }
        return count
    }
    return words
}