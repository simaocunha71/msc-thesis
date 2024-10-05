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

    words := strings.Split(numbers, " ")
    sort.Slice(words, func(i, j int) bool {
        return number_map[words[i]] < number_map[words[j]]
    })

    return strings.Join(words, " ")
}



