    result := make([]int, len(game))
    for i := range game {
        result[i] = int(math.Abs(float64(game[i]-guess[i])))
    }
    return result
}



