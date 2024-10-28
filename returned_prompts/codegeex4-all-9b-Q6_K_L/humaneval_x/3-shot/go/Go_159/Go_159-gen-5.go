    if remaining - need < 0{
        return []int{number + remaining, 0}
    }
    return []int{number + need, remaining - need}
}