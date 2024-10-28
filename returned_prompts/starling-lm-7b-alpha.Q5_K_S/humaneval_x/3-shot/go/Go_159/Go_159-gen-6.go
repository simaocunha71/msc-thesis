    eaten_total := number + min(need, remaining)
    remaining_total := remaining - min(need, remaining)
    return []int{eaten_total, remaining_total}
}



