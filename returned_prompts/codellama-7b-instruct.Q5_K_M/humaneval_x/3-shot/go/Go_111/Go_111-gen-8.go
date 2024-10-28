    var letter_counts = make(map[rune]int)
    var letters = strings.Split(test, " ")

    for _, letter := range letters {
        if _, ok := letter_counts[rune(letter)]; ok {
            letter_counts[rune(letter)] += 1
        } else {
            letter_counts[rune(letter)] = 1
        }
    }
    return letter_counts
}




