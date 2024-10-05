    total := number + remaining
    leftover := remaining - need + number
    if leftover < 0 {
        leftover = 0
    }
    return []int{total, leftover}
}



