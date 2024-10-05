    min_sum  := nums[0]
    cur_sum  := nums[0]
    for _, num := range nums[1:] {
        cur_sum  = int(math.Min(float64(cur_sum+num), float64(num)))
        min_sum  = int(math.Min(float64(min_sum), float64(cur_sum)))
    }
    return min_sum
}



