    words := strings.Fields(txt)
    if len(words) == 1 {
        count := 0
        for _, c := range txt {
            if 'a' <= c && c <= 'z' {
                if int(c-'a')%2 != 0 {
                    count++
                }
            }
        }
        return count
    }
    return words
}



