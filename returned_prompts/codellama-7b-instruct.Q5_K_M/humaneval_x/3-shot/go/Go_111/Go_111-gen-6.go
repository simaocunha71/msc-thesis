    letters := strings.Split(test," ")
    letter_count := make(map[rune]int)

    for _, letter := range letters {
        letter_count[rune(letter[0])] += 1
    }

    return letter_count
}



