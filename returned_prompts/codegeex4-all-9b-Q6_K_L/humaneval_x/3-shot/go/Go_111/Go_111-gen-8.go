    result := make(map[rune]int)
    test = strings.ReplaceAll(test, " ", "")

    for _, c := range test {
        result[c] += 1
    }

    return result
}

