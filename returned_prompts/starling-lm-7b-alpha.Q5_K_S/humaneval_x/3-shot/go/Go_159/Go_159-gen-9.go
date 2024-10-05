    if need > remaining {
        return []int{need + number, 0}
    }
    return []int{number + need, remaining - need}
}



