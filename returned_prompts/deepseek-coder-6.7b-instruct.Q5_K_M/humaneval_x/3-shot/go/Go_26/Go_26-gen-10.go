    result := make([]int, 0)
    appeared := make(map[int]bool)

    for _, num := range numbers {
        if appeared[num] == false {
            result = append(result, num)
            appeared[num] = true
        }
    }

    return result
}



