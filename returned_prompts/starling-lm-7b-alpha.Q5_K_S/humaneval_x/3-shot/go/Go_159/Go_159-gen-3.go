    total := number + need
    left := remaining - need
    if left < 0 {
        left = 0
    }
    return []int{total, left}
}



