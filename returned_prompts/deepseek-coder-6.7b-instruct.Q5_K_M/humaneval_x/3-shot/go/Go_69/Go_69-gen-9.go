    count_map := make(map[int]int)
    max_val := -1

    for _, num := range lst {
        count_map[num] += 1
        if count_map[num] >= num && num > max_val {
            max_val = num
        }
    }

    return max_val
}



