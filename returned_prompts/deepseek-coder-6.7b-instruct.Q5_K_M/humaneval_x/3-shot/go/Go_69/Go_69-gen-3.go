    m := make(map[int]int)
    for _, v := range lst {
        m[v]++
    }

    for i := len(lst) - 1; i >= 0; i-- {
        if m[lst[i]] > lst[i] {
            return lst[i]
        }
    }
    return -1
}



