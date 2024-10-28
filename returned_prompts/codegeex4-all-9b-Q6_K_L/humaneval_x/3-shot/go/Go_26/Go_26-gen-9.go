    result := make([]int, 0)
    mapOfNumbers := make(map[int]bool)

    for _, v := range numbers {
        if _, ok := mapOfNumbers[v]; !ok {
            mapOfNumbers[v] = true
            result = append(result, v)
        }
    }
    return result
}



