    result := make([]int, 0, len(game))
    for i := range game {
        if game[i] == guess[i] {
            result = append(result, 0)
        } else {
            result = append(result, math.Abs(float64(guess[i] - game[i])))
        }
    }
    return result
}