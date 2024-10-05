    total := number + need - remaining
    remaining = remaining - (need - remaining)
    return []int{total, remaining}
}