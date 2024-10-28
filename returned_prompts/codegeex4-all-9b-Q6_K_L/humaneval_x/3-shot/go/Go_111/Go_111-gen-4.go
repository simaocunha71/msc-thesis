    result := make(map[rune]int)
    letter_counter := make(map[rune]int)

    for _, c := range test {
        if c != ' ' {
            letter_counter[c] += 1
        }
    }

    max := 0
    for _, count := range letter_counter {
        if count > max {
            max = count
        }
    }

    for letter, count := range letter_counter {
        if count == max {
            result[letter] = count
        }
    }

    return result
}

