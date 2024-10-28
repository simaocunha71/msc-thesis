    result := make([]int, len(game))
    for i, _ := range game {
        result[i] = int(math.Abs(float64(game[i] - guess[i])))
    }
    return result
}



