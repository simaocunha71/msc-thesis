    res := make([]int, len(game))
    for i :=  range game {
        res[i] = abs(game[i] - guess[i])
    }
    return res
}

func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}

