    total := number
    if need < remaining {
        total += need
        remaining -= need
    } else {
        total += remaining
        remaining = 0
    }
    return []int{total, remaining}
}



