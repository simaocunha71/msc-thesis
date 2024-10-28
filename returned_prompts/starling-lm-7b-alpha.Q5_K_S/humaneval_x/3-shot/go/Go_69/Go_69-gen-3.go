    counter := make(map[int]int)
    for _, i := range lst {
        counter[i]++
    }

    for i := len(lst); i > 0; i-- {
        if counter[i] >= i {
            return i
        }
    }
    return -1
}



