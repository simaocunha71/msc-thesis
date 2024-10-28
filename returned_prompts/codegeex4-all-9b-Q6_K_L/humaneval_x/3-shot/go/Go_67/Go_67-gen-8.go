    numbers := strings.Split(s, " ")
    var apples int
    var oranges int
    for _, number := range numbers {
        if number == "apples" {
            apples, _ = strconv.Atoi(numbers[0])
        } else if number == "oranges" {
            oranges, _ = strconv.Atoi(numbers[2])
        }
    }
    return n - apples - oranges
}


