    numberals := map[string]float64{
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    words := strings.Fields(numbers)

    var values []float64
    for _, word := range words {
        values = append(values, numberals[word])
    }

    sort.Float64s(values)

    var sortedWords []string
    for _, value := range values {
        for word, num := range numberals {
            if num == value {
                sortedWords = append(sortedWords, word)
                break
            }
        }
    }

    return strings.Join(sortedWords, " ")
}

