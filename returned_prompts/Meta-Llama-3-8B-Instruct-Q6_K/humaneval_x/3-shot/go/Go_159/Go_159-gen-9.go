    total := number + need
    leftover := remaining - (total - number)
    if leftover < 0 {
        leftover += remaining
    }
    return []int{total, leftover}
}