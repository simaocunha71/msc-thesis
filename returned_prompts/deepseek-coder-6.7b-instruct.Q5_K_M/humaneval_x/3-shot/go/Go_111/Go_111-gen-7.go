    letter_counts := make(map[rune]int)
    max_count := 0
    max_letters := make(map[rune]int)

    for _, letter := range test {
        if letter != ' ' {
            letter_counts[letter]++
            if letter_counts[letter] > max_count {
                max_count = letter_counts[letter]
            }
        }
    }

    for letter, count := range letter_counts {
        if count == max_count {
            max_letters[letter] = count
        }
    }

    return max_letters
}



