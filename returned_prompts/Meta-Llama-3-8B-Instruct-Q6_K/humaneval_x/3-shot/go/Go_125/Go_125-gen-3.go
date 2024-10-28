    words := strings.Split(txt, " ")
    if len(words) == 1 {
        words = strings.Split(txt, ",")
        if len(words) == 1 {
            result := 0
            for i := 0; i < len(txt); i++ {
                if txt[i] >= 'a' && txt[i] <= 'z' && (i+result)%2 == 1 {
                    result += 1
                }
            }
            return result
        }
    }
    return words
}