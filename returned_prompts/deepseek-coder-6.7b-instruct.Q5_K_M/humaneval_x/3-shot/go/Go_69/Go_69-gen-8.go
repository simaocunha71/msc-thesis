    counts := make(map[int]int)

    for _, num := range lst {
        counts[num]++
    }

    for num, count := range counts {
        if num <= count {
            return num
        }
    }

    return -1
}



