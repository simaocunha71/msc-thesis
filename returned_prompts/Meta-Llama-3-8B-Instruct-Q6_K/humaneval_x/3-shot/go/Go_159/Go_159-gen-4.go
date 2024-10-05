    totalEaten := number + (need - remaining)
    if totalEaten > remaining {
        totalEaten = need
    }
    return []int{totalEaten, remaining - (need - totalEaten)}
}