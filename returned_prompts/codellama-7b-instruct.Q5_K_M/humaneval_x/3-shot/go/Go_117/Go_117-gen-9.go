    result := make([]string, 0)
    words := strings.Split(s, " ")

    for _, word := range words {
        c := 0
        for _, r := range word {
            if !(r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u') {
                c += 1
            }
        }
        if c == n {
            result = append(result, word)
        }
    }
    return result
}



