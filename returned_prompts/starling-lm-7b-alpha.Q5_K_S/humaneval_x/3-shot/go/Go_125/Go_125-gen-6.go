    words := make([]string, 0)

    i := 0
    for _, c := range txt {
        if c == ' ' || c == ',' {
            words = append(words, txt[i:])
            i += 1
        }
    }
    words = append(words, txt[i:])

    if len(words) == 1 {
        result := 0
        for _, c := range words[0] {
            if c >= 'a' && c <= 'z' {
                result += (ord(c) % 2 == 1)
            }
        }
        return result
    }

    return words

    // return (len(words) == 1) * SplitWords(words[0]) + len(words) - 1
}



