    count := make(map[int]int)
    for _, i := range lst {
        count[i]++
    }
    for i := len(lst); i >= 0; i-- {
        if count[i] >= i {
            return i
        }
    }
    return -1
}



