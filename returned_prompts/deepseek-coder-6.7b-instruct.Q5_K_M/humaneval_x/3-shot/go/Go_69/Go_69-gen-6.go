    counter := make(map[int]int)
    max_val := -1

    for _, v := range lst {
        counter[v] += 1
        if counter[v] >= v && v > max_val {
            max_val = v
        }
    }

    return max_val
}



