    words := strings.Split(txt, " ")
    if len(words) == 1 {
        words = strings.Split(txt, ",")
        if len(words) == 1 {
            result := 0
            for i, c := range txt {
                if 'a' <= c && c <= 'z' && (i+1)%2 == 1 {
                    result++
                }
            }
            return result
        }
    }
    return words
}