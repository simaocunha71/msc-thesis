    number_map := map[string]int{
        "zero":  0,
        "one":   1,
        "two":   2,
        "three": 3,
        "four":  4,
        "five":  5,
        "six":   6,
        "seven": 7,
        "eight": 8,
        "nine":  9,
    }

    number_words := strings.Split(numbers, " ")
    number_values := make([]int, len(number_words))

    for i, word := range number_words {
        number_values[i] = number_map[word]
    }

    sort.Ints(number_values)

    for i, value := range number_values {
        for word, num := range number_map {
            if value == num {
                number_words[i] = word
                break
            }
        }
    }

    return strings.Join(number_words, " ")
}



