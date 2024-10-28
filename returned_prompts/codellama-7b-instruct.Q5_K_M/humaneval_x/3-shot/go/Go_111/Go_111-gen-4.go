    letter_counts := make(map[rune]int)
    for _, letter := range test {
        if _, ok := letter_counts[letter]; !ok {
            letter_counts[letter] = 1
        } else {
            letter_counts[letter] += 1
        }
    }
    return letter_counts
}



