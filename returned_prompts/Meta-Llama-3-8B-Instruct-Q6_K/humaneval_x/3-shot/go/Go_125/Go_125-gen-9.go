    words := strings.Split(txt, " ")
    if len(words) == 1 && !strings.Contains(txt, ",") {
        count := 0
        for i := 0; i < len(txt); i++ {
            c := txt[i]
            if 'a' <= c && c <= 'z' {
                if i%2 != 0 {
                    count++
                }
            }
        }
        return count
    }
    return words
}