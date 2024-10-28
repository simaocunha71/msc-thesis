    freq := make(map[int]int)
    for _, num := range lst {
        freq[num]++
    }
    max := -1
    for num, count := range freq {
        if count >= num && num > 0 && num > max {
            max = num
        }
    }
    return max
}