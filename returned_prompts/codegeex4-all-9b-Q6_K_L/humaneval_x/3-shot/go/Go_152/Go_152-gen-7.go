    result := make([]int, 0)
    for i := 0; i < len(game); i++ {
        var difference int = game[i] - guess[i]
        result = append(result, int(math.Abs(float64(difference))))
    }
    return result
}



