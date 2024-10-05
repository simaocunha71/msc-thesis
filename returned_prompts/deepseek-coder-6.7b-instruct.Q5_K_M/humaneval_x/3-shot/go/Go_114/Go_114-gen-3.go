    min_sum := math.MaxInt64
    cur_sum := 0

    for _, num := range nums {
        cur_sum += num
        if cur_sum < min_sum {
            min_sum = cur_sum
        }
        cur_sum = int(math.Max(float64(cur_sum), float64(num)))
    }

    return min_sum
}



