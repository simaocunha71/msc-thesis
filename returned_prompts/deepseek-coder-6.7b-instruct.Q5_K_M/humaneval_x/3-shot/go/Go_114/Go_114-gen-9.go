    min_sum := math.MaxInt32
    cur_sum := 0
    for _, num := range nums {
        cur_sum += num
        if cur_sum < min_sum {
            min_sum = cur_sum
        }
        cur_sum = min(cur_sum, num)
    }
    return min_sum
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}



