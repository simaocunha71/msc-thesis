    result := make([]int, len(game))
    for i, v := range game {
        result[i] = int(math.Abs(float64(guess[i] - v)))
    }
    return result
}