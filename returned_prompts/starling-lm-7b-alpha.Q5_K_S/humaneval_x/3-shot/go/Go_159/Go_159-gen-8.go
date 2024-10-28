    total_eaten := number + need
    remaining -= total_eaten
    if remaining < 0 {
        remaining = 0
    }
    return []int{total_eaten, remaining}
}



