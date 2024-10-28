    hist := make(map[rune]int)
    for _, ch := range strings.Fields(test) {
        hist[[]rune(ch)[0]]++
    }

    max := 0
    for _, v := range hist {
        if v > max {
            max = v
        }
    }

    result := make(map[rune]int)
    for k, v := range hist {
        if v == max {
            result[k] = v
        }
    }

    return result
}



