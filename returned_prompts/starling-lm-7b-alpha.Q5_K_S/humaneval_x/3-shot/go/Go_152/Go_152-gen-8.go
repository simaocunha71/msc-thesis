    result := make([]int, len(game))
    for i, v := range game {
        result[i] = math.Abs(float64(guess[i]) - float64(v))
    }
    return result
}



