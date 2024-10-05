    eaten := number + remaining
    remaining = remaining - (eaten - need)
    return []int{eaten, remaining}
}