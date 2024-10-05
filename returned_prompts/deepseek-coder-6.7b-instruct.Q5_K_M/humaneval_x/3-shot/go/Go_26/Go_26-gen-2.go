    result := make([]int, 0)
    encountered := make(map[int]bool)

    for _, num := range numbers {
        if encountered[num] == false {
            result = append(result, num)
            encountered[num] = true
        }
    }

    return result
}



