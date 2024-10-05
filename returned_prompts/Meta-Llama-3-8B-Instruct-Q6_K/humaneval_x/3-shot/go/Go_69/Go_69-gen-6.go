    count := make(map[int]int)
    max_val := -1

    for _, val := range lst {
        if count[val] == 0 {
            count[val] = 1
        } else {
            count[val] += 1
        }

        if count[val] >= val && val > max_val {
            max_val = val
        }
    }

    if max_val == -1 {
        return -1
    }

    return max_val
}