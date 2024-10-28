    counter := make(map[int]int)

    for _, v := range lst {
        counter[v] += 1
    }

    for i := len(lst); i >= 1; i-- {
        if counter[i] >= i {
            return i
        }
    }
    return -1
}



