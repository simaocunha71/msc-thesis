    txt = strings.Replace(txt, ",", " ", -1)
    words := strings.Split(txt, " ")

    if len(words) > 1 {
        return words
    }

    count := 0
    for _, c := range txt {
        if c >= 'a' && c <= 'z' {
            if int(c-'a')%2 == 1 {
                count++
            }
        }
    }
    return count
}

