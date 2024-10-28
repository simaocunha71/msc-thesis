    words := strings.Split(txt, " ")
    if len(words) == 1 {
        words = strings.Split(txt, ",")
    }
    if len(words) == 1 {
        var count int
        for i := 0; i < len(txt); i++ {
            c := txt[i]
            if 'a' <= c && c <= 'z' {
                if i%2 == 1 {
                    count++
                }
            }
        }
        return count
    }
    return words
}