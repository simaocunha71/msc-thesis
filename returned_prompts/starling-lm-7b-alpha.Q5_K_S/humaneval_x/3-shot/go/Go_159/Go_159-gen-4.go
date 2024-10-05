    total := number + remaining
    leftover := remaining - need
    if leftover < 0 {
        leftover = 0
    }
    return []int{total, leftover}
}




