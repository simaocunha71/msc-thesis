    if need <= remaining {
        return []int{number + need, remaining - need}
    } else {
        return []int{number + remaining, 0}
    }
}



