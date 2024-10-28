    m := make(map[int]int)

    for _, num := range lst {
        m[num]++
    }

    for i := len(lst); i > 0; i-- {
        if val, ok := m[i]; ok && val >= i {
            return i
        }
    }

    return -1
}



