    result := make([]int, len(game))
    for i := 0; i < len(game); i++ {
        result[i] = int(math.Abs(float64(guess[i] - game[i])))
    }
    return result
}