    total := number + remaining
    remaining = remaining - (need - number)
    if remaining < 0 {
        remaining = 0
    }
    return []int{total, remaining}
}



