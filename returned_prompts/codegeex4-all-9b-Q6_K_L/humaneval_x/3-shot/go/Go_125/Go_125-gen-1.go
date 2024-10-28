    words := strings.Split(txt, " ")
    if len(words) > 1 {
        return words
    }

    words = strings.Split(txt, ",")
    if len(words) > 1 {
        return words
    }

    var sum int
    for i := 0; i < len(txt); i++ {
        if txt[i] >= 'a' && txt[i] <= 'z' && (int(txt[i]-'a'))%2 == 1 {
            sum++
        }
    }
    return sum
}