    var frequency_dict map[int]int = make(map[int]int)
    for _, v := range lst {
        frequency_dict[v] += 1
    }

    for k, v := range frequency_dict {
        if k > 0 && v >= k {
            return k
        }
    }

    return -1
}



