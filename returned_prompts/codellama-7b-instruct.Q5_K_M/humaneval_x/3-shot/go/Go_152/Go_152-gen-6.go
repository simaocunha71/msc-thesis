    result := make([]int,len(game))
    for i,score := range game{
        result[i] = abs(score-guess[i])
    }
    return result
}



