    result := make([]int, 0)
    last_occurrence := make(map[int]int)
    for _, number := range numbers {
        if last_occurrence[number] == 0 {
            result = append(result, number)
            last_occurrence[number] = len(result)
        }
    }
    return result
}



