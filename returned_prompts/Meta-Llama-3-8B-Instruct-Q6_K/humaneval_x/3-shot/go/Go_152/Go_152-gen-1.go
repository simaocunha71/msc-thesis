    result := make([]int, 0, len(game))
    for i := 0; i < len(game); i++ {
        diff := int(math.Abs(float64(guess[i] - game[i])))
        result = append(result, diff)
    }
    return result
}
