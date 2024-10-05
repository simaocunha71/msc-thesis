    total := number + need
    left := remaining - total
    if left < 0 {
        left = 0
    }
    return []int{total, left}
}



