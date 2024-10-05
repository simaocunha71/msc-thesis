    counts := make(map[int]int)
    for _, num := range lst {
        counts[num]++
    }
    for i := len(lst) - 1; i >= 0; i-- {
        if counts[lst[i]] > lst[i] {
            return lst[i]
        }
    }
    return -1
}



