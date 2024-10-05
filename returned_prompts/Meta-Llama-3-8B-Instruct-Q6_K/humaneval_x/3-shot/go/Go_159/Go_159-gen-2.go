    eaten := number + need
    left := remaining - (need - eaten)
    if left < 0 {
        left = 0
    }
    return []int{eaten, left}
}