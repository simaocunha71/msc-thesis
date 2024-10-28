    result := make([]int, 0)
    for i := 0; i < len(game); i++ {
        result = append(result, math.Abs(float64(game[i])-float64(guess[i])))
    }
    return result
}



