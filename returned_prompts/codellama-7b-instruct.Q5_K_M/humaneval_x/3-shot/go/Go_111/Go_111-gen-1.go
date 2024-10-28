    runes := []rune(test)
    result := make(map[rune]int)

    for _, r := range runes {
        result[r] += 1
    }

    return result
}



