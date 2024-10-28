    var numberals = map[string]int{
        "zero":    0,
        "one":     1,
        "two":     2,
        "three":   3,
        "four":    4,
        "five":    5,
        "six":     6,
        "seven":   7,
        "eight":   8,
        "nine":    9,
    }

    words := strings.Fields(numbers)
    var numbersList []int
    for _, word := range words {
        numbersList = append(numbersList, numberals[word])
    }
    sort.Ints(numbersList)

    var result string
    for _, num := range numbersList {
        for key, value := range numberals {
            if value == num {
                result += key + " "
            }
        }
    }

    return strings.TrimSpace(result)
}

