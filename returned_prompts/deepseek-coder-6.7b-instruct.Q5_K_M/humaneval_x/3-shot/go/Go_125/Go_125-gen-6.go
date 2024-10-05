    words := strings.Fields(txt)

    if len(words) != 1 {
        return words
    }

    commas := strings.FieldsFunc(txt, func(r rune) bool { return r == ',' })

    if len(commas) != 1 {
        return commas
    }

    count := 0
    for _, c := range txt {
        if 'a' <= c && c <= 'z' {
            if int(c-'a')%2 == 1 {
                count++
            }
        }
    }
    return count
}



