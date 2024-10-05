    frequency_dict := make(map[int]int, len(lst))
    for _, i := range lst {
        frequency_dict[i] += 1
    }

    for i := 1; i <= len(lst); i++ {
        if frequency_dict[i] >= i {
            return i
        }
    }
    return -1
}



