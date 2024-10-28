    eaten := number + remaining
    remaining = remaining - need + number
    if remaining < 0 {
        return []int(eaten + need, 0)
    }
    return []int(eaten, remaining)
}