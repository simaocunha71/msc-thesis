    words := strings.Split(txt, " ")
    if len(words) == 1 {
        words = strings.Split(txt, ",")
        if len(words) == 1 {
            count := 0
            for i := 0; i < len(txt); i++ {
                if 'a' <= txt[i] && txt[i] <= 'z' && i % 2 == 1 {
                    count++
                }
            }
            return count
        }
    }
    return words
}