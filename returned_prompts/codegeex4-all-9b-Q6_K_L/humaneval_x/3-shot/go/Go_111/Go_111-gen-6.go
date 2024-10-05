    letters := strings.Fields(test)

    counts := make(map[rune]int)

    for _, letter := range letters {
        counts[rune(letter[0])] += 1
    }

    return counts
}

