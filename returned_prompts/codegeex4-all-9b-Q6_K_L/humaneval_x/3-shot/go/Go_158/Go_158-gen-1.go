    result := make([]string, 0)
    max := 0
    for _, w := range words {
        s := make(map[rune]bool)
        for _, c := range w {
            if _, ok := s[c]; !ok {
                s[c] = true
            }
        }

        if len(s) > max {
            result = []string{w}
            max = len(s)
        } else if len(s) == max {
            result = append(result, w)
        }
    }

    sort.Strings(result)
    return result[0]
}



