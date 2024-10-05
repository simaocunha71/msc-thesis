    uniqueNumbers := make([]int, 0, len(numbers))
    numberMap := make(map[int]struct{})

    for _, number := range numbers {
        if _, ok := numberMap[number]; !ok {
            numberMap[number] = struct{}{}
            uniqueNumbers = append(uniqueNumbers, number)
        }
    }
    return uniqueNumbers
}



