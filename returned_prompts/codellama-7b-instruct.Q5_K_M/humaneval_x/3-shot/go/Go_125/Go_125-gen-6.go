    words := strings.Fields(txt)
    if len(words) != 0 {
        return words
    }
    if strings.Contains(txt, ",") {
        words = strings.Split(txt, ",")
    }
    var count int = 0
    for _, c := range txt {
        if c >= 'a' && c <= 'z' {
            if c%2 != 0 {
                count += 1
            }
        }
    }
    return count
}



