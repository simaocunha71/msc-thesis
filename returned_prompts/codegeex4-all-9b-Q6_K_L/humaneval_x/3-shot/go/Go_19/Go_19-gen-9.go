    numberals := map[string]int {
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

    numbers_splitted := strings.Split(numbers, " ")
    numbers_int := make([]int, 0)

    for _, number := range numbers_splitted {
        numbers_int = append(numbers_int, numberals[number])
    }

    sort.Ints(numbers_int)

    numbers_sorted := make([]string, 0)

    for _, number := range numbers_int {
        for key, value := range numberals {
            if number == value {
                numbers_sorted = append(numbers_sorted, key)
            }
        }
    }
    return strings.Join(numbers_sorted, " ")
}



