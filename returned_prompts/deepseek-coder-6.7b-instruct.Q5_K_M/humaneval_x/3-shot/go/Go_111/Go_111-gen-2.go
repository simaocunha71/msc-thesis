    letter_counts := make(map[rune]int)
    max_count := 0
    result := make(map[rune]int)

    for _, letter := range test {
        _, ok := letter_counts[letter]
        if ok {
            letter_counts[letter]++
        } else {
            letter_counts[letter] = 1
        }
        if letter_counts[letter] > max_count {
            max_count = letter_counts[letter]
        }
    }

    for letter, count := range letter_counts {
        if count == max_count {
            result[letter] = count
        }
    }

    return result
}



