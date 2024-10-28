    countMap := make(map[int]int)
    for _, num := range lst {
        countMap[num]++
    }
    max := -1
    for num, count := range countMap {
        if num > 0 && num <= count {
            max = num
        }
    }
    return max
}