    words := strings.Split(test, " ")
    frequency := make(map[rune]int)

    for _, word := range words {
        for _, letter := range word {
            frequency[letter]++
        }
    }

    max_frequency := 0
    max_letters := make(map[rune]int)

    for letter, count := range frequency {
        if count > max_frequency {
            max_frequency = count
            max_letters = map[rune]int{letter: count}
        } else if count == max_frequency {
            max_letters[letter] = count
        }
    }

    return max_letters
}