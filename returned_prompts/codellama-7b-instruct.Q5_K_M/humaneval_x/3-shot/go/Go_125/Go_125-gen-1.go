    words := strings.Split(txt, " ")
    if len(words) > 0 {
        return words
    }

    if strings.ContainsAny(txt, ",") {
        words = strings.Split(txt, ",")
        return words
    }

    count := 0
    for _, c := range txt {
        if c >= 'a' && c <= 'z' {
            count += 1
        }
    }
    return count
}



