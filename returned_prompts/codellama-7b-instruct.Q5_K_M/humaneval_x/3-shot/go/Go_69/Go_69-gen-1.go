    if len(lst) == 0 {
        return -1
    }

    freq := make(map[int]int)
    for _, value := range lst {
        freq[value] += 1
    }

    for key := range freq {
        if key >= 1 && freq[key] >= key {
            return key
        }
    }
    return -1
}



