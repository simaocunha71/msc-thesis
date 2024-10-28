    result := make([]int, len(game))
    for i := 0; i < len(game); i++ {
        result[i] = math.Abs(float64(game[i] - guess[i]))
    }
    return result
}



