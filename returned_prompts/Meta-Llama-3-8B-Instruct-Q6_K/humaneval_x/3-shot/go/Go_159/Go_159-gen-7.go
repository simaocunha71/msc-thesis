    eaten := number + need
    leftover := remaining - (eaten - remaining)
    if leftover < 0 {
        leftover = 0
    }
    return []int{eaten, leftover}
}