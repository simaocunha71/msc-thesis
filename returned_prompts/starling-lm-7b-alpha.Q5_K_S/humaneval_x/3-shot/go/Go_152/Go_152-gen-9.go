    result := make([]int, len(game))
    for i,g := range game {
        result[i] = math.Abs(float64(g) - float64(guess[i]))
    }
    return result
}



