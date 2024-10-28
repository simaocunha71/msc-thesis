    words := strings.Split(txt, " ")
    if len(words) == 1 {
        words = strings.Split(txt, ",")
        if len(words) == 1 {
            var count int
            for i := 0; i < len(txt); i++ {
                c := txt[i]
                if c >= 'a' && c <= 'z' {
                    if (int(c) - 'a') % 2 == 1 {
                        count++
                    }
                }
            }
            return int(count)
        }
    }
    return words
}