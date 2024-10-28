    totalEaten := number + (remaining - (remaining % need))
    leftCarrots := remaining - ((remaining / need) * need)
    return []int{totalEaten, leftCarrots}
}